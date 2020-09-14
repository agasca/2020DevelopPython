#try catch
print("Ingrese su numerator: ")
number = int(input())
print("entre a denominator: ")
denom = int(input())

a = '''
try:
    quotient = number / denom
    print(quotient)
except:
    print("cannot execute")
'''

try:
    quotient = number / denom
    print(quotient)
except ZeroDivisionError:
    print("Error: Can't divided by zero")
finally:
    print("end")
    #close files or release resources