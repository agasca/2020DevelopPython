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

class Checking(Account):
    def __init__(self, acctNumber, balance, fee):
        Account.__init__(self, acctNumber, balance)
        self.fee = fee
    def __str__(self):
        retStr = "Account type :\n"
        retStr += Account.__str__(self)
        return retStr
    def getFree(self):
        return self.fee
    def desposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("fondos insuficientes")
        else:
            self.balance = self.balance - amount - self.fee


ca = Checking("123", 500, 0.50)
print(ca)
ca.withdraw(100)
print(ca)
ca.desposit(23)
print(ca)