a = input("enter the number: ")
b = input("enter one more: ")
a = int(a)
b = int(b)

try:
    print(a / b)
except ZeroDivisionError:
    print("b can not be zero")