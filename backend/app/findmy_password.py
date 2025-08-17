import json
import base64
import requests

# to maintain the integrity of the password, we will obfuscate it using base64 encoding for this project.
# this is only to demostrate the concept of obfuscation and should not be used in production code, we only feed the actual password to the program because it is not part of the list in order to protect access to the VM. 
actual_password = input("PASSWORD: ")
with open('password_key.json', 'w') as pass_key:
    # encode (obfuscate)
    actual_password = base64.b64encode(actual_password.encode()).decode()
    print("Encoded:", actual_password)
    pass_data = pass_key.write(json.dumps({"pass_key": actual_password}))

# web scraping the password list from KoreLogic's SecLists repository
# this is a list of common passwords that can be used for testing purposes.
url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Permutations/korelogic-password.txt'

data = requests.get(url)
passwords = data.text.splitlines()

for password in passwords:
    with open('passwords.txt', 'a') as password_file:
        password_file.write(password + '\n')
        
with open('password_key.json', 'r') as pass_key:
    # decode (restore)
    decoded = base64.b64decode(actual_password.encode()).decode()

# adding the actual password to the passwords.txt file
with open('passwords.txt', 'a') as password_file:
    password_file.write(decoded + '\n')