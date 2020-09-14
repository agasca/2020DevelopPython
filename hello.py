import os
import math
# Print welcome message
# C:\Users\lenovo\Desktop\2020\2020DeveloPython
#print("Hello")
files = os.popen("dir *.py")
for file in files:
    print(file)

print(math.fabs(-123.45))