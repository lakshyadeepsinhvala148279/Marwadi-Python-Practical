#multiple Inheritance: Encryption + Authentication ->SecureSystem

class Encryption:
    def encrypt(self):
        print("Data is Encrypted")

class Authentication:
    def authenticate(self):
        print("user Authentication is perfomed")

class SecureSystem(Encryption, Authentication):
    def secure_data(self):
        print("System provide secure data access")

s = SecureSystem()
s.encrypt()
s.authenticate()
s.secure_data()
