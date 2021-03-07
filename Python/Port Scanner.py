import socket
import time
import threading
import sys

print("-"*20)
print("Python Port Scanner")
print("-"*20)

Raw_Target = input("Enter Target IP Or Host: ")
Start_Port = int(input("Enter Start Port: "))
End_Port = int(input("Enter End Port: "))

print()

Start_Time = time.time()

try:
    Fixed_Target = socket.gethostbyname(Raw_Target)
except socket.gaierror:
    print("Could Not Resolve Host")
    sys.exit()

print('[*] Starting Port Scan On', Raw_Target)
print()

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    conn = s.connect_ex((Fixed_Target, port))
    if (not conn):
        print("[+] Port {} Is Open".format(port))
    s.close()

for port in range(Start_Port, End_Port+1):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()

End_Time = time.time()
print()
print("Scan Completed In:", End_Time - Start_Time, "Seconds")
input()
