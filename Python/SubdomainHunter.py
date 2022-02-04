import dns.resolver
import sys

usage = f"[*] Usage: python3 {sys.argv[0]} <domain> <list>"

try:
	domain = sys.argv[1]
	domainlist = sys.argv[2]
except:
	print(usage)
	quit()

try:
	subdomainlist = [ x.strip() for x in open(domainlist, 'r', encoding='latin-1') if x ]
except:
	print('[-] List not found')

def main(subdo):
	try:
		ip = dns.resolver.resolve(f'{subdo}.{domain}', 'A')
		if ip:
			print(f"[+] {subdo}.{domain}")
	except dns.resolver.NXDOMAIN:
		pass
	except dns.resolver.NoAnswer:
		pass
	except KeyboardInterrupt:
		print("\n[-] Aborted")
		quit()

print("[+] Valid Subomains: \n")

for subdomain in subdomainlist:
	main(subdomain)