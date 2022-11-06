#Itertools
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=2)
print(list(prod))
print('________________________________________________')

from itertools import permutations
a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))
print('________________________________________________')

from itertools import combinations
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
print('________________________________________________')

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
print('________________________________________________')

from itertools import accumulate
import operator
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=operator.mul) #Eliminando func los suma por default 
print(a)
print(list(acc))

acc = accumulate(a, func=max)
print(a)
print(list(acc))
print('________________________________________________')

from itertools import groupby

def small3(x):
    return x < 3

group_obj = groupby(a, key=small3)
for key, value in group_obj:
    print(key, list(value))


persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))


