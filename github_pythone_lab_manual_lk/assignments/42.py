print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import whois

domain = "google.com"
w = whois.whois(domain)

print("WHOIS Lookup Result:")
print(w)
