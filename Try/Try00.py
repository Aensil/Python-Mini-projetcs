#collections
from collections import Counter

a = "aaaabbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.most_common(2))
print(my_counter.most_common(1)[0][0])
print('________________________________________________')

from collections import namedtuple
Score = namedtuple('Score', 'x,y')
pt = Score(1, -4)
print(pt)
print(pt.x, pt.y)
print('________________________________________________')

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 1
ordered_dict['c'] = 1
ordered_dict['d'] = 1
ordered_dict['a'] = 1
print(ordered_dict)
print('________________________________________________')

from collections import defaultdict
d = defaultdict(list)  #
d['a'] = 1
d['b'] = 2
print(d['c'])   #lista vacia

#d = {}
#print(d['c'])    #KeyError: 'c'
print('________________________________________________')

from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print('Append: ', d)

d.popleft()
print('Pop: ', d)

d.clear()
print('clear: ', d)

d.append(1)
d.append(2)

d.extendleft([4, 5, 6])
print('extend: ', d)

