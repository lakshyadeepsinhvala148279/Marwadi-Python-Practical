print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import hashlib

data = "CyberSecurity2026"

md5_hash = hashlib.md5(data.encode()).hexdigest()
sha256_hash = hashlib.sha256(data.encode()).hexdigest()

print(f"Original String: {data}")
print(f"MD5 Hash: {md5_hash}")
print(f"SHA-256 Hash: {sha256_hash}")
