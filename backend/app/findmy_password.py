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
    
    actual_password = input("PASSWORD: ")
    with open(passKey, 'r') as pass_key:
        pass_file = json.load(pass_key)

    # encode (obfuscate)
    encoded_pass = base64.b64encode(actual_password.encode()).decode()
    pass_file['pass_key'] = encoded_pass

    with open(passKey, "w") as pass_key:
        json.dump(pass_file, pass_key, indent=4)  
        
    # web scraping the password list from KoreLogic's SecLists repository
    # this is a list of common passwords that can be used for testing purposes.
    url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Permutations/korelogic-password.txt'

    data = requests.get(url)
    passwords = data.text.splitlines()
    passwords_list = os.path.join(base_dir, "passwords.txt")

    # writing the passwords to a file
    for password in passwords:
        with open(passwords_list, 'w') as password_file:
            password_file.write(password + '\n')
    
    # adding encrypted password to password_key.json
    with open(passKey, 'r') as pass_key:
        pass_file = json.load(pass_key)
    
    decoded = pass_file['pass_key']
    # decode (restore)
    decoded_pass = base64.b64decode(decoded.encode()).decode()

    # adding the actual password to the passwords.txt file
    with open(passwords_list, 'a') as password_file:
        password_file.write(decoded_pass + '\n')