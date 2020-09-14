ag = '''
# account
# C:\Users\lenovo\Desktop\2020\2020DeveloPython# abstract data type POO
'''
class Account:
    def __init__(self, acctNumber, balance):
        self.acctNumber = acctNumber
        self.balance = balance

    def __str__(self):
        return "Account number :" +  str(self.acctNumber) + "\n" + \
            "Balance :" + str(self.balance)
    
    def deposit(self, amount):
        self.balance += amount
#        
class Checking(Account):
    def __init__(self, acctNumber, balance, fee):
        Account.__init__(self, acctNumber, balance)
        self.fee = fee
    def __str__(self):
        retStr = "Account type : Checking\n"
        retStr += Account.__str__(self)
        return retStr
    def getFree(self):
        return self.fee
    def withdraw(self, amount):
        if amount > self.balance:
            print("fondos insuficientes")
        else:
            self.balance = self.balance - amount - self.fee
#
class Savings(Account):
    def __init(self, acctNumber, balence):
        Account.__init__(self, acctNumber, balence)

    def __str__(self):
        retStr = "Account type : Savings\n"
        retStr += Account.__str__(self)
        return retStr
    def withdraw(self, amount):
        if amount > self.balance:
            print("fondos insuficientes")
        else:
            self.balance = self.balance - amount


ca = Checking("123", 500, 0.50)
print(ca)
ca.withdraw(100)
print(ca)
ca.deposit(23)
print(ca)
sa = Savings("456", 1000)
sa.withdraw(250)
print(sa)
sa.deposit(125)
print(sa)

accounts = [ca, sa]
print("\nDesplegar todas las cuentas")
for i in range(0,len(accounts)):
    print(accounts[i])