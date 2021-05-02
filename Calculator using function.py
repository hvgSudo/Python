def add():
    a = int(input("\nEnter number 1: "))
    b = int(input("Enter number 2: "))
    c = a + b
    return(c)

def sub():
    a = int(input("\nEnter number 1: "))
    b = int(input("Enter number 2: "))
    c = a - b
    return(c)

def mult():
    a = int(input("\nEnter number 1: "))
    b = int(input("Enter number 2: "))
    c = a * b
    return(c)

def div():
    a = int(input("\nEnter number 1: "))
    b = int(input("Enter number 2: "))
    c = a / b
    return(c)

def rem():
   a = int(input("\nEnter number 1: "))
   b = int(input("Enter number 2: "))
   c = a % b
   return(c)
  
while 1 == 1:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Quotient")
    print("5. Remainder")
    print("6. Quit")
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
        break
    else:
        print("Wrong Input")

print("\n\t\tThank you for using Calculator")
