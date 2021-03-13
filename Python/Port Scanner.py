import socket
import time
import threading
import sys
from termcolor import colored

# Be Sure To Pip Install Termcolor

Open = 0

print(colored("-"*20, 'yellow'))
print(colored("Python Port Scanner", 'green'))
print(colored("-"*20, 'yellow'))

try:
    Raw_Target = input(colored("[*] Enter Target IP Or Host: ", 'white'))
    Start_Port = int(input(colored("[*] Enter Start Port: ", 'white')))
    End_Port = int(input(colored("[*] Enter End Port: ", 'white')))
except KeyboardInterrupt:
    print()
    print()
    print(colored("[-] Aborted", 'red'))
    sys.exit()
print()

if End_Port > 65535:
    print(colored("[-] Invalid Ports", 'red'))
    sys.exit()

elif Start_Port > 65535:
    print(colored("[-] Invalid Ports", 'red'))
    sys.exit()

Start_Time = time.time()

try:
    Fixed_Target = socket.gethostbyname(Raw_Target)
except socket.gaierror:
    print(colored("[-] Host Could Not Be Resolved", 'red'))
    sys.exit()

print('[*] Starting TCP Port Scan On', Fixed_Target)
print()

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    conn = s.connect_ex((Fixed_Target, port))
    if (not conn):
        print(colored("[+] Port {}/tcp Is Open".format(port), 'green'))
        global Open
        Open = 1
    s.close()

try:
    for port in range(Start_Port, End_Port+1):
        thread = threading.Thread(target = scan_port, args = (port,))
        thread.start()

except KeyboardInterrupt:
    print()
    print(colored("[-] Aborted", 'red'))
    sys.exit()
    
time.sleep(1)

if Open == 0:
	print(colored("[-] No Open Ports Found In Range", 'red'))

End_Time = time.time()
print()
print("Scan Completed In:", End_Time - Start_Time, "Seconds")
time.sleep(3)
