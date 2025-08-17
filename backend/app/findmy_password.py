import json
import base64
import requests
import os

def finder():
    # to maintain the integrity of the password, we will obfuscate it using base64 encoding for this project.
    # this is only to demostrate the concept of obfuscation and should not be used in production code, we only feed the actual password to the program because it is not part of the list in order to protect access to the VM. 
    
    # file directory
    base_dir = os.path.dirname(__file__)  # directory of app/__init__.py
    passKey = os.path.join(base_dir, "password_key.json")
    
    actual_password = input("PASSWORD: ").strip()
    with open(passKey, 'w') as pass_key:
        # encode (obfuscate)
        actual_password = base64.b64encode(actual_password.encode()).decode()
        pass_data = pass_key.write(json.dumps({"pass_key": actual_password}))
        #pass_file['pass_key'] = encoded_pass
        
    # web scraping the password list from KoreLogic's SecLists repository
    # this is a list of common passwords that can be used for testing purposes.
    url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/worst-passwords-2017-top100-slashdata.txt'

    data = requests.get(url)
    passwords = data.text.splitlines()
    
    base_dir = os.path.dirname(__file__)
    passwords_list = os.path.join(base_dir, "passwords.txt")

    # writing the passwords to a file
    for password in passwords:
        with open(passwords_list, 'a') as password_file:
            password_file.write(password + '\n')
    
    # adding encrypted password to password_key.json
    with open(passKey, 'r') as pass_key:
        # decode (restore)
        decoded = base64.b64decode(actual_password.encode()).decode().strip()
        
    # adding the actual password to the passwords.txt file
    with open(passwords_list, 'a') as password_file:
        password_file.write(decoded)