import requests
import re

url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Default-Credentials/ssh-betterdefaultpasslist.txt'

data = requests.get(url)
passwords = data.text.splitlines()

password_bank = {}
for key_value in passwords:
    match = re.search(r'([^:]+):([^:]+)', key_value)

    if match:
        user = match.group(1)
        password = match.group(2)
        password_bank[user] = password
        print(f"user:", user)
        print(f"password:", password)

with open('passwords.txt', 'w') as file:
    for user, password in password_bank.items():
        file.write(f"{password}\n")
