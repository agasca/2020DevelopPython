ag = '''
# student
# C:\Users\lenovo\Desktop\2020\2020DeveloPython
# C:\Users\lenovo\Desktop\2020\2020DeveloPython# abstract data type POO
'''
class Student:
    #fields - name, id, grade[list]
    grades = []
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def addGrades(self, grade):
        self.grades.append(grade)
    
    def showGrades(self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + '\n'
        return grds

stud = Student('al','123')
stud.addGrades(88)
stud.addGrades(85)
stud.addGrades(89)
stud.addGrades(80)
print(stud.showGrades())
