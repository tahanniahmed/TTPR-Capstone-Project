import os
import requests
image_url = "https://images3.memedroid.com/images/UPLOADED184/566a1ba50f28c.jpeg"

# setting the path to download
desktop_path = r"C:\Users\michael_account\Desktop"

file_name = "hello_there.jpg"
file_path = os.path.join(desktop_path, file_name)

# creating a directory if it doesn't exist
os.makedirs(desktop_path, exist_ok=True)

# error handling for the request
response = requests.get(image_url)

# creating the file
with open(file_path, "wb") as file:
    file.write(response.content)

# output response
print(f"Image saved to: {file_path}")