print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import socket
import dns.resolver

domain = "google.com"

ip = socket.gethostbyname(domain)
print(f"IP Address of {domain}: {ip}")

print("\nDNS A Records:")
answers = dns.resolver.resolve(domain, 'A')
for rdata in answers:
    print(rdata.to_text())
