import socket
import time
import threading
import sys

Open = 0

print("-"*20)
print("Python Port Scanner")
print("-"*20)

Raw_Target = input("[*] Enter Target IP Or Host: ")
Start_Port = int(input("[*] Enter Start Port: "))
End_Port = int(input("[*] Enter End Port: "))

print()

if End_Port > 65535:
    print("[-] Invalid Ports")
    sys.exit()

elif Start_Port > 65535:
    print("[-] Invalid Ports")
    sys.exit()

Start_Time = time.time()

try:
    Fixed_Target = socket.gethostbyname(Raw_Target)
except socket.gaierror:
    print("[-] Host Could Not Be Resolved")
    sys.exit()

print('[*] Starting TCP Port Scan On', Fixed_Target)
print()

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    conn = s.connect_ex((Fixed_Target, port))
    if (not conn):
        print("[+] Port {}/tcp Is Open".format(port))
        global Open
        Open = 1
    s.close()

for port in range(Start_Port, End_Port+1):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()
    
time.sleep(1)

if Open == 0:
	print("[-] No Open Ports Found In Range")

End_Time = time.time()
print()
print("Scan Completed In:", End_Time - Start_Time, "Seconds")
time.sleep(3)