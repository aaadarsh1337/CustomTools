import socket
import time
import threading
import sys
from colorama import init, Fore, Back, Style

init(convert=True)

# Be Sure To Pip Install 'colorama'

Open = 0

# A Good Looking Banner :)

print(Fore.CYAN + "Welcome To Python Port Scanner!" + Style.RESET_ALL)
print()

# Try To Get Input

try:
    Raw_Target = input(Fore.BLUE + '[*]' + " Enter Target IP Or Host: " )
    Raw_Start_Port = input(Fore.BLUE + '[*]' + " Enter Start Port: ")
    Raw_End_Port = input(Fore.BLUE + '[*]' + " Enter End Port: ")

# If There Is A Keyboard Interrupt

except KeyboardInterrupt:
    print()
    print()
    print(Fore.RED + "[-] Aborted" + Style.RESET_ALL)
    sys.exit()
print()

try:
    Start_Port = int(Raw_Start_Port)
    End_Port = int(Raw_End_Port)

except ValueError:
    print(Fore.RED + "[-] Invalid Ports" + Style.RESET_ALL)
    sys.exit()

# Checking If The Ports Are Less Than Or Equal To 65535(Total TCP Ports)

if End_Port > 65535:
    print(Fore.RED + "[-] Invalid Ports" + Style.RESET_ALL)
    sys.exit()

elif Start_Port > 65535:
    print(Fore.RED + "[-] Invalid Ports" + Style.RESET_ALL)
    sys.exit()

# Starting Time For Printing Scan Time

Start_Time = time.time()

# Trying To Convert Hostname To IP If It Is Not

try:
    Fixed_Target = socket.gethostbyname(Raw_Target)
except socket.gaierror:
    print(Fore.RED + "[-] Could Not Resolve Host" + Style.RESET_ALL)
    sys.exit()

# One More Banner :)

print(Fore.CYAN + '[+] Starting TCP Port Scan On', Fixed_Target + Style.RESET_ALL)
print()

# Defining Scan Port Function

def scan_port(port):
    # AF_INET And SOCK_STREAM Work For TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Setting Timeout Because Of Lag Sometime :(
    s.settimeout(0.5)
    # Trying To Connect To Target
    # If Status Is 0, It Means That The Port Is Open
    status = s.connect_ex((Fixed_Target, port))
    # Defining If Statement To Check If It Responded Or Not
    if status == 0:
        # Banner Again :)
        print(Fore.GREEN + "[+] Port {}/tcp Is Open".format(port) + Style.RESET_ALL)
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
    print(Fore.RED + "[-] Aborted" + Style.RESET_ALL)
    sys.exit()

# Timeout For Name Sake :)
    
time.sleep(1)

# If No Ports Are Open

if Open == 0:
	print(Fore.RED + "[-] No Open Ports Found In Range" + Style.RESET_ALL)

# Getting Scan Time
End_Time = time.time()
print()
print(Fore.LIGHTWHITE_EX + "Scan Completed In:", End_Time - Start_Time, "Seconds")
time.sleep(3)

# Happy Hacking :)
