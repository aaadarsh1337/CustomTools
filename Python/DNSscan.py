from ast import Index
import dns.resolver
import sys

usage = f"\n[*] Usage: python3 {sys.argv[0]} <DomainName> (Note: Please don't add http:// or https:// in the domain.)"

records = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']

try:
    domain = sys.argv[1]
except IndexError:
    print(usage)
    quit()

for record in records:
    try:
        answer = dns.resolver.resolve(domain, record)
        print(f"\n[+] {record}: \n")
        for server in answer:
            print(server.to_text())
    except dns.resolver.NoAnswer:
        pass
    except KeyboardInterrupt:
        print("\n[-] Aborted")
        quit()
    except dns.resolver.NXDOMAIN:
        print(f"\n[-] {domain} does not exist (Note: Please don't add http:// or https:// in the domain.)")
        quit()