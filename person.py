ag = '''
# student
# C:\Users\lenovo\Desktop\2020\2020DeveloPython
# C:\Users\lenovo\Desktop\2020\2020DeveloPython# abstract data type POO
'''
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def  __str__(self):
        return self.name + ' ' + self.sex + ' ' + str(self.age)
    
    def changeAge(self):
        self.age +=1    #self.age = self.age + 1

    def changeName(self, name):
        self.name = name

pesron1 = Person('jane doe', 'f', 23)
pesron2 = Person('joe dsmith', 'm', 33)
print("persona 2: " + str(pesron2))
print("persona 1: " + str(pesron1))
pesron1.changeAge()
print("persona 1: " + str(pesron1))
pesron1.changeName('Olivia')
print("persona 1: " + str(pesron1))
