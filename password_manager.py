import json
from cryptography.fernet import Fernet

# Load key
with open("key.key", "rb") as file:
    key = file.read()

fernet = Fernet(key)

# Load existing passwords
try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
except:
    passwords = {}

while True:
    print("\n1. Add Password")
    print("2. View Password")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")
        encrypted_password = fernet.encrypt(password.encode()).decode()
        passwords[website] = {
            "username": username,
            "password": encrypted_password
        }
        with open("passwords.json", "w") as file:
            json.dump(passwords, file, indent=4)
        print("Password saved securely!")

    elif choice == "2":
        website = input("Website: ")
        if website in passwords:
            username = passwords[website]["username"]
            encrypted_password = passwords[website]["password"]
            decrypted_password = fernet.decrypt(
                encrypted_password.encode()
            ).decode()
            print("\nUsername:", username)
            print("Password:", decrypted_password)
        else:
            print("No record found.")

    elif choice == "3":
        break

    else:
        print("Invalid choice!")
