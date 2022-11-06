x = [1, 2, 3, 4]
y = x.copy()

x[0] = 'a'
print(x)
print(y)
print('________________________________________________')

a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
# also possible in a list
myList = [1, 2, 3, 4, 5]
print("Initial list :", myList)
myList[0], myList[1] = myList[1], myList[0]
print("Modified list:", myList)
print('________________________________________________')

my_list = ["I", "am", "awesome"]

# bad
a = ""
for i in my_list:
    a += i + " "
print(a)

# good
a = " ".join(my_list)
print(a)
print('________________________________________________')

name = "Eric"
age = 25
a = f"Hello, {name}. You are {age}."
print(a)
pi = 3.14159
a = f"Pi is {pi:.3f}"
print(a)
# f-Strings are evaluated at runtime, which allows expressions
a = f"The value is {2*60}"
print(a)

