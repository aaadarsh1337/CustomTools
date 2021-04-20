import urllib.request
import json
import socket
import sys
import time
from requests import get

try:
    IP = get('https://ipapi.co/ip').text
    print("You Public IP: " + IP)

except:
    print("[-] Error: No Internet")
    time.sleep(5)
    sys.exit()
    
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
    print("[-] Error: Could Not Connect To Target")
    time.sleep(5)
    sys.exit()

except KeyboardInterrupt:
    print("[-] Aborted")
    time.sleep(5)

try:
    URL = "http://ip-api.com/json/"
    Response = urllib.request.urlopen(URL + Fixed_Target + "?fields=query,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,isp,timezone")
    Data = Response.read()
    Value = json.loads(Data)

except urllib.error.URLError:
    print("[-] Error: No Internet")
    time.sleep(5)
    sys.exit()

except KeyboardInterrupt:
    print("[-] Aborted")
    time.sleep(5)

try:
    if 'query' in Value:
        print("[+] Target: " + Value['query'])
    if 'message' in Value:
        print("[+] Message: " + Value['message'])
    if 'continent' and 'continentCode' in Value:
        print("[+] Continent: " + Value['continent'] + "(" + Value['continentCode'] + ")")
    if 'country' and 'countryCode' in Value:
        print("[+] Country: " + Value['country'] + "(" + Value['countryCode'] + ")")
    if 'region' and 'regionName' in Value:
        print("[+] Region: " + Value['regionName'] + "(" + Value['region'] + ")")
    if 'city' and 'zip' in Value:
        print("[+] City: " + Value['city'] + "(" + Value['zip'] + ")")
    if 'lat' in Value:
        print("[+] Latitude: " + str(Value['lat']))
    if 'lon' in Value:
        print("[+] Longitude: " + str(Value['lon']))
    if 'isp' in Value:
        print("[+] ISP: " + Value['isp'])
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
