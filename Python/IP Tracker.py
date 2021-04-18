import os
import urllib.request
import json
import socket
import sys
import time

try:
    Raw_Target = input("Enter Target Hostname Or IP: ")
    print()
except KeyboardInterrupt:
    print("[-] Aborted")
    time.sleep(5)
    sys.exit()

try:
    Fixed_Target = socket.gethostbyname(Raw_Target)
except socket.gaierror:
    print("[-] Could Not Connect To Target")
    time.sleep(5)
    sys.exit()

except KeyboardInterrupt:
    print("[-] Aborted")
    time.sleep(5)

try:
    URL = "http://ipapi.co/"
    Response = urllib.request.urlopen(URL + Fixed_Target + '/json/')
    Data = Response.read()
    Value = json.loads(Data)

except urllib.error.URLError:
    print("[-] Could Not Connect To Internet")
    time.sleep(5)
    sys.exit()

except KeyboardInterrupt:
    print("[-] Aborted")
    time.sleep(5)

try:
    if 'ip' in Value:
        print("[+] Target: " + Value['ip'] + "(" + Value['version'] + ")")
    if 'reason' in Value:
        print("[+] Message: " + Value['reason'])
    if 'continent_code' in Value:
        print("[+] Continent: " + Value['continent_code'])
    if 'country_name' and 'country_code' in Value:
        print("[+] Country: " + Value['country_name'] + "(" + Value['country_code'] + ")")
    if 'region' and 'region_code' in Value:
        print("[+] Region: " + Value['region'] + "(" + Value['region_code'] + ")")
    if 'city' and 'postal' in Value:
        print("[+] City: " + Value['city'] + "(" + Value['postal'] + ")")
    if 'latitude' in Value:
        print("[+] Latitude: " + str(Value['latitude']))
    if 'longitude' in Value:
        print("[+] Longitude: " + str(Value['longitude']))
    if 'country_calling_code' in Value:
        print("[+] Country Calling Code: " + str(Value['country_calling_code']))
    if 'org' in Value:
        print("[+] ISP: " + Value['org'])
    if 'timezone' in Value:
        print("[+] Time Zone: " + Value['timezone'])
    
    print()
    print("[*] OSINT Completed")
    time.sleep(10)
    sys.exit()

except KeyboardInterrupt:
    print()
    print("[-] Aborted")
    time.sleep(5)
