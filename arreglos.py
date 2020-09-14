
ag = '''
# name
# C:\Users\lenovo\Desktop\2020\2020DeveloPython
# Arreglos
https://www.programiz.com/python-programming/array
'''
import array as arr
a = arr.array('d', [1.1, 3.5, 4.5])
print("ejemplo de arreglo")
print(a)
for number in a:
    print(number)

print("ejemplo de lista")

ag = '''
# Listas
'''
print("for each")
numbers = [10,20,30,40,50,60,70]
for number in numbers:
    print(number)

print("for next")
for i in range(0,len(numbers)):
    print(numbers[i])

print("ejemplo de tuple")

ag = '''
# tuples
'''
numeros = (1,2,3,4,5)
print(numeros)
sum = 0
for num in numeros:
    sum =  sum + num
    print(sum)
print("la suma es:" + str(sum))

palabras = ("hola", " como ", "estas.")
for palabra in palabras:
    print(palabra)
print(palabras[1])

ag = '''
# dictionary
'''
contactos = {'al':'123', 'luis':'234','jose':'345'}
print(contactos.keys())
print(contactos.values())
for key in contactos.keys():
    print(key + " valor: " + contactos[key])


ag = '''
# loop anidado 1
'''
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " es primo"
   i = i + 1
print "fin!"    


ag = '''
# loop anidado 2
the code appearing below shows two nested loops, an outer for loop over the values of i and an inner for loop over the values of j to multiply inside the inner loop all nine elements of a 3x3 matrix A by a factor f that changes according to the outer loop iteration.
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
equals
[
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
'''
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f = 1
print(A)
for i in range(0, 3):
    f *= 10
    for j in range(0, 3):
       A[i][j] *= f
print(A)

ag = '''
# for next
'''
print("For next nested 1")
for x in range(1, 3):
    for y in range(1, 3):
        print('%d * %d = %d' % (x, y, x*y))

print("For next nested 2")
for x in range(3):
    for y in range(3):
        print('%d * %d = %d' % (x, y, x*y))        