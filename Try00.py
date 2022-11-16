n=3
x=0
y=1
l=[]
l.append(x)
l.append(y)

if n >= 2:
    for i in range(n-1):
        S = l[-1] - l[-2]
        l.append(S)

Z = l[n]
print(Z)