def add():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a + b
    return(c)

def sub():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a - b
    return(c)

def mult():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a * b
    return(c)

def div():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a / b
    return(c)

def rem():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a % b
    return(c)

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Quotient")
print("5. Remainder")
d = int(input("Enter your choice: "))

if d == 1:
    print("The sum of two numbers: ",add())
elif d == 2:
    print("The difference between the two numbers: ",sub())
elif d == 3:
    print("The product of two numbers: ",mult())
elif d == 4:
    print("The quotient of two numbers: ",round(div(),2))
elif d == 5:
    print("The remainder of two numbers: ",rem())
else:
    print("Wrong Input")
