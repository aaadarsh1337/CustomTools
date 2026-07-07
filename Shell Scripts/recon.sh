#!/bin/bash

if [ $# -gt 2 ]; then
	echo "[*] Usage: ./recon.sh <domain>"
	exit 1
fi

if [ ! -d  "thirdlevels" ]; then
	mkdir thirdlevels
fi

if [ ! -d  "scans" ]; then 
	mkdir scans
fi

echo "[*] Gathering subdomains with Amass"
amass enum -d $1 -o final.txt

echo "[*] Compiling third-level domains"
cat final.txt | grep -Po "([\w-]+\.[\w-]+\.[\w-]+)$" | sort -u > third-level.txt

echo "[*] Gathering complete third-level domains with Amass"
for domain in $(cat third-level.txt); do amass enum -d $domain -o thirdlevels/domains.txt; cat thirdlevels/domains.txt | sort -u >> final.txt; done

if [ $# -eq 2 ];
then
	echo "[*] Probing for alive domains"
	cat final.txt | sort -u | grep -v $2 | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ":443" > nmap_probed.txt
	cat final.txt | sort -u | grep -v $2 | httprobe -p https > probed.txt

else
	echo "[*] Probing for alive domains"
	cat final.txt | sort -u | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ":443" > nmap_probed.txt
	cat final.txt | sort -u | httprobe -p https > probed.txt
fi

cat probed.txt | sort -u
cat nmap_probed.txt | sort -u
cat final.txt | sort -u

echo "[*] Scanning for open ports"
nmap -iL nmap_probed.txt -oA scans/scanned.txt

echo "[*] Running EyeWitness"
eyewitness -f $(pwd)/probed.txt --web --no-prompt

echo "[+] Scan Completed";
