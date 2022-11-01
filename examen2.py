def isvalid(s: str)->bool:
    result=None
    x = [i for i in s]
    Errors = []
    vali = {')':'(', ']':'[', '}':'{'}
    for i in range(0, len(x)):
        if x[i] == '(' or x[i] == '{' or x[i] == '[':
            Errors.append(x[i])
        else:
            if vali.get(x[i]) == Errors[-1]:
                Errors.pop()
            else:
                pass
    if len(Errors) == 0:
        result = True
    else:
        pass
    return result
if __name__=="__main__":
    line =input()
    if isvalid(line):
        print("valid")
    else:
        print("invalid") 