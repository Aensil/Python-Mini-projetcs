x = input('Escriba el texto: ')
x = str(x)
#x = x.strip().split()
x = list(x)
x.sort(reverse=True) #ordernar en reversa
n = ''
for i in range(len(x)):
    n = n + str(x[i])

print(n)