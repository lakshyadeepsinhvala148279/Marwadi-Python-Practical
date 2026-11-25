#Hieararchical Inheritance: SecureSystem -> IDS and IPS

class SecureSystem:
    def monitor(self):
        print("Network is bing monitored")

class IDS(SecureSystem):
    def detect(self):
        print("IDS detect suspicious activity")

class IPS(SecureSystem):
    def prevent(self):
        print("IPS prevent malicious activity")

i = IDS()
p = IPS()
i.monitor()
i.detect()
p.prevent()
