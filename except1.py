import sys


def calc(op1, op2, op):
    if op == '+\r\n':
        return op1 + op2
    elif op == '-\r\n':
        return op1 - op2
    elif op == '*\r\n':
        return op1 * op2
    elif op == '/\r\n':
        return op1 / op2

cont = 'y'
while cont != 'n\r\n':
    print("enter first number  : ")
    num1 = int(input())
    print("enter second number :" )
    num2 = int(input())
    print("enter operation symbol +,-,*,/ : ")
    op = sys.stdin.readline()
    #op = input()
    if op == '/\r\n' and num2 == 0:
        print("Cannot divide by zero")
        continue
    else:
        print(calc(num1, num2, op))
    print("do you want to continiue (y/n)?")
    cont = sys.stdin.readline()


#apertura de archivo
a='''
import os
print("nter file name")
name = input() #ver 3.0
while not os.path.isfile(name)
    print("file does not exist")
    print("nter file name")
    name = input() #ver 3.0
file =  open(name, 'r')
for line in file:
        print(line, end='')
'''