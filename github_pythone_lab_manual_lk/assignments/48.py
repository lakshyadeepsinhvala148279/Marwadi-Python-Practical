print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import socket

target = "127.0.0.1"
ports = [21, 22, 80, 443, 3306]

print(f"Scanning target: {target}")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: Open")
    else:
        print(f"Port {port}: Closed")
    s.close()
