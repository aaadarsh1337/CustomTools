[*] Creating A Pentest Dropbox
[*] It Is Mainly Used For Internal Peneteration Testing

[+] Steps:

[*] Create An Azure Account

[*] On The Main(Home) Machine:

1. Open Azure
2. Under Azure Services, Click On Virtual Machines
3. Create Virtual Machine

[*] Basics:

-Subscription: Azure Subscription 1
-Resource Group: Create New Named Anything
-Vitual Machine Name: OpenVPN
-Region: Your Region
-Availability Options: No Infastructure Redundancy Required
-Image: Ubuntu Server 18.04 LTS
-Size: Change size --> B1s
-Administrator Account: You Can Choose Any Of The Options And Set It Up
-Public Inbound Ports: Allow Selected Ports
-Select Inbound Ports: 22, 80, 443

[*] Disks:

-OS Disk Type: Standard HDD

[*] Networking:

-Public IP: Create New --> Assignment: Static

[*] Now Just Click Review + Create
[*] Click On Create
[*] Wait For It To Completely Deploy
[*] Goto Home And Virtual Machines, And You Should See A New VM
[*] Now Click On It's Name, Goto Networking Under Settings
[*] Add Inbound Port Rule

-Source: Any
-Source Port Ranges: *
-Destination: Any
-Destination Port Ranges: 1194
-Protocol: UDP
-Action: Allow
-Priority: 350
-Name: Port_1194
-Description: Empty

[*] Click On Add
[*] Now SSH Into That VM Using PuTTY Or CMD(Using The Public IP Address Displayed)
[*] Do su ~
[*] Now Run:

wget https://github.com/angristan/openvpn-install/openvpn-install.sh
chmod +x openvpn-install.sh
./openvpn-install.sh

[*] Now:
[*] IP: It Should Automatically Print Yours. Hit Enter
[*] Protocol: UDP
[*] Port: 1194
[*] DNS: 1.1.1.1
[*] Name: dropbox
[*] Press Any Key And Wait. 
[*] Now Run:

systemctl enable openvpn

[*] Now, Cat The File:

cat dropbox.ovpn

[*] Copy The Contents To Your Windows Machine As Well As The Kali Dropbox As: dropbox.ovpn
[*] On Our Kali Machine(The Dropbox):

1. Open Terminal
2. sudo apt update -y && sudo apt dist-upgrade -y
3. Till It Completes, Open A New Terminal And Run:

cp dropbox.ovpn /etc/openvpn/openvpn.conf
systemctl enable openvpn
systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

4. Now After The Update, Install RDP Of Your Choice:

sudo apt install xrdp -y
service xrdp start
service xrdp-sesman start
systemctl enable xrdp

[*] Now You Can Test:

sudo openvpn dropbox.ovpn
ifconfig

[*] You Should See tun0. Done!
[*] Reboot(shutdown -r now)
[*] This Will Automatically Do Everything After Reboot Because Of systemctl
[*] Now You Can Try RDP(Make Sure That Your Main Machine Is Also Connected To VPN)

1. Open Remote Desktop Connection
2. Now In The IP, There Is No Need To Use The tun0 IP. You Can Use wlan0 Or eth0
3. Login Using The Credentials. 

[*] We Have Successfully Made A Dropbox!
