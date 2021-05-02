import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def power(a, b):
    return(a ** b)
def fac(a):
    return math.factorial(a)

def trig():
    print("\n")
    print("1. sin x")
    print("2. cos x")
    print("3. tan x")
    a = int(input("Enter your choice: "))
    if a == 1:
        b = float(input("Enter x in degrees: "))
        print("{} {:.3f} = {:.3f}".format("sin", b, math.sin(math.radians(b))))
    elif a == 2:
        b = float(input("Enter x in degrees: "))
        print("{} {:.3f} = {:.3f}".format("cos", b, math.cos(math.radians(b))))
    elif a == 3:
        b = float(input("Enter x in degrees: "))
        print("{} {:.3f} = {:.3f}".format("tan", b, math.tan(math.radians(b))))

def inv():
    print("\n")
    print("1. sin inverse x")
    print("2. cos inverse x")
    print("3. tan inverse x")
    a = int(input("Enter your choice: "))
    if a == 1:
        b = float(input("Enter x in degrees: "))
        print("{} {:.3f} = {:.3f}".format(
            "sin ^ -1", b, math.asin(math.radians(b))))
    elif a == 2:
        b = float(input("Enter x in degrees: "))
        print("{} {:.3f} = {:.3f}".format(
            "cos ^ -1", b, math.acos(math.radians(b))))
    elif a == 3:
        b = float(input("Enter x in degrees: "))
        print("{} {:.3f} = {:.3f}".format(
            "tan ^ -1", b, math.atan(math.radians(b))))

def thm(a):
    return math.log(a)

def th(a):
    return math.log10(a)

def t(a, b):
    return math.log(a,b)

while True:
    print("\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power of a number")
    print("6. Factorial")
    print("7. Trigonometric functions")
    print("8. Inverse triginomeetric functions")
    print("9. Natural log (ln)")
    print("10. log")
    print("11. log to any base")
    print("12. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        number_1 = float(input("Enter float 1: "))
        number_2 = float(input("Enter float 2: "))
        print("\n{} + {} = {:.3f}".format(number_1, number_2, add(number_1, number_2)))
    elif choice == 2:
        number_1 = float(input("Enter float 1: "))
        number_2 = float(input("Enter float 2: "))
        print("\n{} - {} = {:.3f}".format(number_1, number_2, subtract(number_1, number_2)))
    elif choice == 3:
        number_1 = float(input("Enter float 1: "))
        number_2 = float(input("Enter float 2: "))
        print("\n{} x {} = {:.3f}".format(number_1, number_2, multiply(number_1, number_2)))
    elif choice == 4:
        number_1 = float(input("Enter float 1: "))
        number_2 = float(input("Enter float 2: "))
        print("\n{} / {} = {:.3f}".format(number_1, number_2, divide(number_1, number_2)))
    elif choice == 5:
        number_1 = float(input("Enter the float: "))
        number_2 = float(input("Enter the power: "))
        print("\n{} raised to {}: {:.3f}".format(number_1, number_2, power(number_1, number_2)))
    elif choice == 6:
        number_3 = int(input("Enter a whole number: "))
        print("\n{}! = {}".format(number_3, fac(number_3)))
    elif choice == 7:
        trig()
    elif choice == 8:
        inv()
    elif choice == 9:
        number_1 = float(input("Enter the number: "))
        print("{} {:.3f} = {:.3f}".format("ln", number_1, thm(number_1)))
    elif choice == 10:
        number_1 = float(input("Enter the number: "))
        print("{} {:.3f} = {:.3f}".format("log", number_1, th(number_1)))
    elif choice == 11:
        number_1 = float(input("Enter the number: "))
        number_3 = int(input("Enter natural number as base: "))
        print("{} {:.3f} to the base {} = {:.3f}".format("log", number_1, number_3, t(number_1, number_3)))
    elif choice == 12:
        print("Thank you")
        break
