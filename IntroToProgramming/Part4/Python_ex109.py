try:
    a = input("enter the number: ")
    b = input("enter one more: ")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Input Error. Inter the number, except Zero, not String!")