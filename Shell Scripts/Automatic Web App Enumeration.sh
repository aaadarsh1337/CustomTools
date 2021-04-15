#!/bin/bash

url=$1

if [ ! -d "$url"];then
    mkdir $url
fi

if [ ! -d "$url/recon"];then
    mkdir $url/recon
fi

if [ ! -d "$url/recon/screenshots"];then
    mkdir $url/recon/screenshots
fi

echo "[*] Harvesting Subdomains With Assetfinder"
assetfinder $url >> $url/recon/assets.txt
cat $url/recon/assets.txt | grep $1 >> $url/recon/final.txt
rm $url/recon/assets.txt

echo "[*] Harvesting Subdomains With Amass"
amass enum -d $url >> $url/recon/f.txt
sort -u $url/recon/f.txt >> final.txt
rm $url/recon/f.txt

echo "[*] Probing For Alive Domains"
cat $url/recon/final.txt | sort -u | httprobe -s | sed 's/https\?:\/\///' >> $url/recon/a.txt
sort -u $url/recon/a.txt > $url/recon/alive.txt
rm $url/recon/a.txt

echo "[*] Taking Screenshots Of Live Domains"
gowitness file -s $url/recon/alive.txt -d $url/recon/screenshots/