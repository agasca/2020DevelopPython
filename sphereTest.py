# sphereTest
# C:\Users\lenovo\Desktop\2020\2020DeveloPython

sample1 = '''
from sphere import *

print ("enter the radius of the sphere")
radius = int(input())
print ("the area is" + str(area(radius)))
print ("the volume us " + str(volume(radius)))
'''

#sample2
import sphere

print ("enter the radius of the sphere")
radius = int(input())
print ("the area is" + str(sphere.area(radius)))
print ("the volume us " + str(sphere.volume(radius)))