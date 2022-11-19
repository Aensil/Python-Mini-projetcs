mapa = {
    "0": "0",
    "1": "1",
    "6": "9",
    "8": "8",
    "9": "6"
}

print('-------------------------------')

x = int(input('Agrege la cantidad de numeros: '))

max_num = 10
for i in range(x-1):
    max_num = 10 * max_num

results = []

for i in range(max_num):
    n = str(i)
    F = str(n)
    F = F[::-1]
    n = list(n)
    F = list(F)

    for j in range(len(n)):
        if i % 2 == 0:
            F[j] = mapa.get(F[j])
        else:
            u = i/2
            u = int(u)
            u = u - 1
            if u != j:
                F[j] = mapa.get(F[j])
    
    if ((F == n) and (len(n) == x)):
        results.append(i)

print(results)
print('-------------------------------')