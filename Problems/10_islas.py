import pandas as pd
import numpy as np

print('-------------------------------')
'''
data = {
    0:[0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    1:[0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    2:[0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    3:[1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    4:[0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    5:[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    6:[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    7:[1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    8:[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    9:[1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
}
'''
data = {
    0:[0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    1:[0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    2:[0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    3:[1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    4:[0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    5:[0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    6:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    7:[1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    8:[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    9:[1, 0, 1, 0, 0, 0, 0, 0, 1, 1]
}


df_isla = pd.DataFrame(data)
#df_isla.to_csv('all.csv')          #exporta el dataframe as a csv
#df_isla=pd.read_csv("all.csv")#leer de archivo

#print(df_isla.info())
print(df_isla)
print('-------------------------------')

result = 0

add = 3
L = [1, 2] #doesn't matter
while add != 1:
    if len(L) == 0: # just to added her in the firs cicle
        add = add - 1

    delete = [] #save al of add conexions to delete at the end

    L = []
    #Borra all with one conexion
    for i in df_isla.index:
        for j in df_isla.index:
            node = 0 #number of 1 conexions from node
            x = 0 #number of borders
            if df_isla.loc[i, j] == 1:

                try:
                    if df_isla.loc[i-1, j] == 0:
                        node = node + 1
                except:
                    x = x + 1

                try:
                    if df_isla.loc[i+1, j] == 0:
                        node = node + 1
                except:
                    x = x + 1

                try:
                    if df_isla.loc[i, j-1] == 0:
                        node = node + 1
                except:
                    x = x + 1

                try:
                    if df_isla.loc[i, j+1] == 0:
                        node = node + 1
                except:
                    x = x + 1

                if ((node == 3) and (x == 0)):   #borra all conexions with 3 zeros if 0 borders, prevent add = 2 and those conexions
                    L.append(node)
                    delete.append([i,j]) #save of list to delete at the end of the cicle

                elif ((node == add) and (x == 0)):
                    L.append(node)
                    delete.append([i,j]) #save of list to delete at the end of the cicle
                
                elif ((node == add) and (x == 1) and (2 == add)):
                    L.append(node)
                    delete.append([i,j]) #save of list to delete at the end of the cicle

    for p in range(len(delete)):
        df_isla.loc[delete[p][0], delete[p][1]] = 0

print('-------------------------------')
print(df_isla)
print('-------------------------------')

for i in df_isla.index:
    for j in df_isla.index:
        if df_isla.loc[i, j] == 1:
            result = result + 1
print('-------------------------------')
print('El numero total de islas es: ', result)
rr = input('presione enter para salir: ')