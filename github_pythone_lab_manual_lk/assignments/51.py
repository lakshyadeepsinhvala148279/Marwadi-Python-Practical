print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import os
import platform

ip_list = ["127.0.0.1", "8.8.8.8", "192.168.1.250"]

param = "-n 1" if platform.system().lower() == "windows" else "-c 1"

for ip in ip_list:
    response = os.system(f"ping {param} {ip} > nul")
    if response == 0:
        print(f"IP {ip}: UP")
    else:
        print(f"IP {ip}: DOWN")
