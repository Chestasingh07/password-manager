import os

FILE = "passwords.txt"

def save_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(FILE, "a") as f:
        f.write(f"{website} | {username} | {password}\n")

    print("Password saved successfully!\n")

def view_passwords():
    if not os.path.exists(FILE):
        print("No passwords saved yet!\n")
        return

    with open(FILE, "r") as f:
        data = f.readlines()

    print("\nStored Passwords:")
    for line in data:
        print(line.strip())
    print()

def search_password():
    site = input("Enter website to search: ")

    if not os.path.exists(FILE):
        print("No data found!\n")
        return

    found = False
    with open(FILE, "r") as f:
        for line in f:
            if site.lower() in line.lower():
                print("Found:", line.strip())
                found = True

    if not found:
        print("No match found!\n")

def main():
    while True:
        print("==== Password Manager ====")
        print("1. Save Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            save_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
