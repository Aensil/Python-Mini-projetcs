#funtion reduce in list
from functools import reduce

print('-------------------------------')
x = int(input('Escriba el numero de elementos de la lista: '))
l = []
for i in range(x):
    n = int(input('agrege el elemento : '))
    l.append(n)

sum = reduce(lambda a, b: a + b, l)

all = sum / (len(l))
print('-------------------------------')
print('La suma total es: ', sum)
print('El promedio es: ', all)
print('-------------------------------')