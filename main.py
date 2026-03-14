# NexusAuth IAM - Main Application

from auth import authenticate

def main():
    print("Welcome to NexusAuth IAM System")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate(username, password):
        print("Access Granted")
    else:
        print("Access Denied")

if __name__ == "__main__":
    main()
