def calPoints(obs)->int:
    result = None
    L=[]
    for i in range (len(ops)):
        if ops[i]=='+':
            try:
                L.append(float(L[-1]) + float(L[-2]))
            except:
                print('For + there any 2 last number')
        elif ops[i]=='D':
            try:
                L.append(float(L[-1])*2)
            except:
                print('for D there any last score')
        elif ops[i]=='C':
            try:
                L.pop()
            except:
                print("For C there any previous score")
        else:
            try:
                L.append(float(ops[i]))
            except:
                print('only print number')
    result=0.0
    for i in range(len(L)):
        result=result + float(L[i])
    return result
if __name__=='__main__':
    line=input()
    ops=line.strip().split()
    calPoints(ops)
    print(calPoints(ops))
