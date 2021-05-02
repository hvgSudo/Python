import math

def add():
    print("\n")
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    return(a + b)

def sub():
    print("\n")
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    return(a - b)

def mult():
    print("\n")
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    return(a * b)

def div():
    print("\n")
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    return(a / b)

def rem():
    print("\n")
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    return(a % b)

def power():
    print("\n")
    a = float(input("Enter the number: "))
    b = float(input("Enter the power: "))
    return(math.pow(a,b))

def fac():
    print("\n")
    a = int(input("Enter the number: "))
    return(math.factorial(a))

def trig():
    print("\n")
    print("1. sin x")
    print("2. cos x")
    print("3. tan x")
    a = int(input("Enter your choice: "))
    if a == 1:
        b = float(input("Enter x: "))
        return(math.sin(b))
    elif a == 2:
        b = float(input("Enter x: "))
        return(math.cos(b))
    elif a == 3:
        b = float(input("Enter x: "))
        return(math.tan(b))

def inv():
    print("\n")
    print("1. sin inverse x")
    print("2. cos inverse x")
    print("3. tan inverse x")
    a = int(input("Enter your choice: "))
    if a == 1:
        b = float(input("Enter x: "))
        return(math.asin(b))
    elif a == 2:
        b = float(input("Enter x: "))
        return(math.acos(b))
    elif a == 3:
        b = float(input("Enter x: "))
        return(math.atan(b))

def hcf():
    print("\n")
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    return(math.gcd(a,b))

def thm():
    print("\n")
    a = float(input("Enter the number: "))
    return(math.log(a))

def th():
    print("\n")
    a = float(input("Enter the number: "))
    return(math.log10(a))

def t():
    print("\n")
    a = float(input("Enter the number: "))
    b = int(input("Enter the base: "))
    return(math.log(a,b))

def dia():
    print("\n")
    a = float(input("Enter the angle in radians: "))
    return(math.degrees(a))

def deg():
    print("\n")
    a = float(input("Enter the angle in degrees: "))
    return(math.radians(a))
  
while 1 == 1:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Quotient")
    print("5. Remainder")
    print("6. Any power of any number")
    print("7. Factorial")
    print("8. Trigonometric functions")
    print("9. Inverse Trigonometric functions")
    print("10. Greatest Common Divisor or HCF")
    print("11. Natural Logarithm (ln)")
    print("12. Logarithm to the base 10 (log)")
    print("13. Logarithm to the base other than 10 and e")
    print("14. Convert Radian to Degree")
    print("15. Convert Degree to Radian")
    print("16. Exit")
    d = input("Enter your choice: ")

    try:
        d = int(d)
    except:
        print("\nInvalid input, only numbers accepted")
        continue

    if d == 1:
        print("\nThe sum of two numbers: ",add())
    elif d == 2:
        print("\nThe difference between the two numbers: ",sub())
    elif d == 3:
        print("\nThe product of two numbers: ",mult())
    elif d == 4:
        print("\nThe quotient of two numbers: ",round(div(),2))
    elif d == 5:
        print("\nThe remainder of two numbers: ",rem())
    elif d == 6:
        print("\nThe evaluation of the given number with its power: ",power())
    elif d == 7:
        print("\nThe factorial of the given number: ",fac())
    elif d == 8:
        print("\nThe value of the given triginometric identity: ",trig())
    elif d == 9:
        print("\nThe value of the given inverse",end = " ")
        print("trigonometric identity: ",inv())
    elif d == 10:
        print("\nThe HCF of the given numbers: ",hcf())
    elif d == 11:
        print("\nThe natural logarithm of the given number: ",thm())
    elif d == 12:
        print("\nThe log of the given number: ",th())
    elif d == 13:
        print("\nThe logarithm of the given number: ",t())
    elif d == 14:
        print("\nThe degree equivalent of the given radian: ",dia())
    elif d == 15:
        print("\nThe radian equivalent of the given degree: ",deg())
    elif d == 16:
        break
    else:
        print("Wrong Input")

print("\n\t\tThank you for using Calculator")
