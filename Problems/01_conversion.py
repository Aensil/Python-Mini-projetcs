
x = input('Por favor escriba la longitud en metros: ')

try:
    x = float(x)
except:
    print('Solo escriba los numeros')

L = []
print('-------------------------------')
n = x/0.0254
L.append(n)
n = n/12
L.append(n)
n = n/3
L.append(n)
n = n/1760
L.append(n)

F = ['pulgadas', 'pies', 'yardas', 'millas']
for i in range(len(F)):
    k = int(L[i]*10000)
    k = k/10000
    print(f'Su medida en {F[i]} es: {k}')
print('-------------------------------')
