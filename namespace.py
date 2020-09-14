#namespace
# C:\Users\lenovo\Desktop\2020\2020DeveloPython
import newton


def square(number):
    print("not from the newton module")
    return number * number

num = 12
print ("From newton module")
print (newton.square(num))
print ("From main process ")
print (square(num))
