import socket
import time
import threading
import sys
from termcolor import colored

# Be Sure To Pip Install Termcolor

Open = 0

# A Good Looking Banner :)

print(colored("-"*20, 'yellow'))
print(colored("Python Port Scanner", 'green'))
print(colored("-"*20, 'yellow'))

# Try To Get Input

try:
    Raw_Target = input(colored("[*] Enter Target IP Or Host: ", 'white'))
    Start_Port = int(input(colored("[*] Enter Start Port: ", 'white')))
    End_Port = int(input(colored("[*] Enter End Port: ", 'white')))

# If There Is A Keyboard Interrupt

except KeyboardInterrupt:
    print()
    print()
    print(colored("[-] Aborted", 'red'))
    sys.exit()
print()

# Checking If The Ports Are Less Than Or Equal To 65535(Total TCP Ports)

if End_Port > 65535:
    print(colored("[-] Invalid Ports", 'red'))
    sys.exit()

elif Start_Port > 65535:
    print(colored("[-] Invalid Ports", 'red'))
    sys.exit()

# Starting Time For Printing Scan Time

Start_Time = time.time()

# Trying To Convert Hostname To IP If It Is Not

try:
    Fixed_Target = socket.gethostbyname(Raw_Target)
except socket.gaierror:
    print(colored("[-] Host Could Not Be Resolved", 'red'))
    sys.exit()

# One More Banner :)

print('[*] Starting TCP Port Scan On', Fixed_Target)
print()

# Defining Scan Port Function

def scan_port(port):
    # AF_INET And SOCK_STREAM Work For TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Setting Timeout Because Of Lag Sometime :(
    s.settimeout(0.5)
    # Trying To Connect To Target
    conn = s.connect_ex((Fixed_Target, port))
    # Defining If Statement To Check If It Responded Or Not
    if (not conn):
        # Banner Again :)
        print(colored("[+] Port {}/tcp Is Open".format(port), 'green'))
        # Defined Open Because If There Are No Ports Open, It Wont Print Anything
        global Open
        Open = 1
    # Closing Connection
    s.close()

# Using Threading Because Only The For Statement Will Take Forever:(

try:
    for port in range(Start_Port, End_Port+1):
        # Defining Thread
        thread = threading.Thread(target = scan_port, args = (port,))
        # Starting Thread
        thread.start()

# If User Does Keyboard Interrupt

except KeyboardInterrupt:
    print()
    print(colored("[-] Aborted", 'red'))
    sys.exit()

# Timeout For Name Sake :)
    
time.sleep(1)

# If No Ports Are Open

if Open == 0:
	print(colored("[-] No Open Ports Found In Range", 'red'))

# Getting Scan Time

End_Time = time.time()
print()
print("Scan Completed In:", End_Time - Start_Time, "Seconds")
time.sleep(3)

# Happy Hacking :)