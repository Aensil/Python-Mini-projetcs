#Define dictionary for conversión
L = {
    'uno':1,
    'dos':2,
    'tres':3,
    'cuatro':4,
    'cinco':5,
    'seis':6,
    'siete':7,
    'ocho':8,
    'nueve':9,
    'diez':10,
    'once':11,
    'doce':12,
    'trece':13,
    'catorce':14,
    'quince':15,
    'dieciseis':16,
    'diecisiete':17,
    'dieciocho':18,
    'diecinueve':19,
    'veinte':20,
    'veintiuno':21,
    'veintidos':22,
    'veintitres':23,
    'veinticuatro':24,
    'veinticinco':25,
    'veintiseis':26,
    'veintisiete':27,
    'veintiocho':28,
    'veintinueve':29,
    'treinta':30,
    'cuarenta':40,
    'cincuenta':50,
    'sesenta':60,
    'setenta':70,
    'ochenta':80,
    'noventa':90,
    'cien':100,
    'ciento':100,
    'doscientos':200,
    'trescientos':300,
    'cuatrocientos':400,
    'quinientos':500,
    'seiscientos':600,
    'setecientos':700,
    'ochocientos':800,
    'novecientos':900
}

print('-------------------------------')
x = input("Escriba el numero sin tildes: ")
x = str(x)
x = x.strip().split()

negative = 0 #0 meaning positive
result = 0

#Delete all 'y'
for i in range(len(x)):
    try:    #List out of range due to pop delting elements
        if x[i] == 'y':
            x.pop(i)
    except:
        pass


for i in range(len(x)):
    k = L.get(x[i])
    if x[i] == 'menos':
        negative = 1
    #evaluationa and adding the number
    elif k != None:
        result = result + L.get(x[i])
    elif ((x[i] == 'mil') and (result == 0)):
        result = result + 1000
    elif x[i] == 'mil':
        result = result*1000
    else:
        pass

if negative == 1:
    result = result * -1


print(result, '.')
print('-------------------------------')
#menos nueve mil trescientos veintidos