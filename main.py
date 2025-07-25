
# main.py
from modules import port_scanner, brute_forcer

def main():
    print("=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Force Login")
    choice = input("Choose a module: ")

    if choice == "1":
        target = input("Target IP/Host: ")
        ports = input("Enter ports (e.g., 22,80,443): ")
        port_list = [int(p.strip()) for p in ports.split(",")]
        port_scanner.scan_ports(target, port_list)

    elif choice == "2":
        url = input("Login URL: ")
        username = input("Username: ")
        username_field = input("Form field name for username: ")
        password_field = input("Form field name for password: ")
        wordlist_path = input("Path to password wordlist: ")

        try:
            with open(wordlist_path, "r") as f:
                passwords = f.readlines()
            brute_forcer.brute_force_login(url, username_field, password_field, username, passwords)
        except FileNotFoundError:
            print("❌ Wordlist file not found.")

    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
