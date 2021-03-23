import socket
import sys

Host = input("Enter Hostname: ")

try:
    IP = socket.gethostbyname(Host)
    print("IP Found: " + IP)

except socket.gaierror:
    print("Could Not Resolve Host")
    sys.exit