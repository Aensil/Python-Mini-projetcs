x = input('Amount of money: ')
y = input('Amount of years: ')

try:
    x = float(x)
    y = float(y)
except:
    print('Solo escriba los numeros')

print('-------------------------------')
n = x * ((1.0 + 0.05) ** y)
print('The amount of money you had is: ', int(n))