from security import authenticate, encrypt_text
from system_controller import NorthshoreSystem

def login_screen():
    print("=== Northshore Logistics System ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    user = authenticate(username, password)
    if user:
        print(f"\nWelcome, {user['username']} ({user['role']})")
        return user
    else:
        print("\nInvalid username or password.")
        return None