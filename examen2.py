import imp
from msilib.schema import Error


def isvalid(s: str)->bool:
    result=None
    x = [i for i in s]
    Errors = []
    vali = {')':'(', ']':'[', '}':'{'}
    for i in range(0, len(x)):
        try:
            if x[i] == '(' or x[i] == '{' or x[i] == '[':
                Errors.append(x[i])
            else:
                if vali.get(x[i]) == Errors[-1]:
                    Errors.pop()
                else:
                    pass
        except:
            Errors.append('l')
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