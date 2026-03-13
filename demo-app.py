print("NexusAuth IAM Demo")

def login(user):
    if user == "admin":
        print("Admin access granted")
    else:
        print("User access granted")

login("admin")
