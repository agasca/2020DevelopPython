ag = '''
# rectangle.py
# C:\Users\lenovo\Desktop\2020\2020DeveloPython# abstract data type POO
'''
class Shape:
    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord
    
    def __str__(self):
        return 'x :' + str(self.x) + ' y :' + str(self.y)

    def move(self, x1, y1):
        self.x = self.x + x1
        self.y = self.y + y1

class Rectangle(Shape): #inherit from ()
    def __init__(self, xcoord, ycoord, width, heigth):
        Shape.__init__(self, xcoord, ycoord)
        self.width = width
        self.heigth = heigth

    def __str__(self):
        retStr = Shape.__str__ (self)
        retStr += ', width :' + str(self.width) + \
            ', heigth :' + str(self.heigth)
        return retStr

rec = Rectangle(5,10,8,9)
print(rec)
rec.move(13,14)
print(rec)
