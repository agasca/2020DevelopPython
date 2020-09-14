ag = '''
# name
# C:\Users\lenovo\Desktop\2020\2020DeveloPython
# C:\Users\lenovo\Desktop\2020\2020DeveloPython# abstract data type POO
'''
# Class
class Name:
    #constructor method - instantiation
    def __init__(self, first, middle, last):
        #attributes
        self.first = first
        self.middle = middle
        self.last = last
    
    #method to-string method
    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last
    #method 
    def lastFirst(self):
        return self.last + ' ' + self.first + ' ' + self.middle
    #method 
    def initials(self):
        return self.first[0] + ' ' + self.middle[0]  + ' ' + self.last[0] 


#main
aName = Name('Nanc','liz','Smith') 
print(aName)
print(aName.lastFirst())
print(aName.initials())

yourName = Name('alberto', 'gasca', 'bernal')
print("yourName is :" + str(yourName))
print("yourName is :" + str(yourName.lastFirst()))
print("yourName is :" + str(yourName.initials()))
