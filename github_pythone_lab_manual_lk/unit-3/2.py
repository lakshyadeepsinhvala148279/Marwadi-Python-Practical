#multilevel Inhertitence: security ->Networksecurity ->firewall

class Security:
    def protect(self):
        print("System protection is enable")

class NetworkSecurity(Security):
    def monitor_network(self):
        print("Network Traffic is monitored")

class Firewall(NetworkSecurity):
    def block_traffic(self):
        print("malicious traffic is blocked")

f = Firewall()
f.protect()
f.monitor_network()
f.block_traffic()
