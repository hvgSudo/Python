import Cal
n = int(input("Enter number 1: "))
m = int(input("Enter number 2: "))

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
        print("\nThe sum of two numbers: ",Cal.add(n,m))
    elif d == 2:
        print("\nThe difference between the two numbers: ",Cal.sub(n,m))
    elif d == 3:
        print("\nThe product of two numbers: ",Cal.mult(n,m))
    elif d == 4:
        print("\nThe quotient of two numbers: ",round(Cal.div(n,m),2))
    elif d == 5:
        print("\nThe remainder of two numbers: ",Cal.rem(n,m)) 
    elif d == 6:
        break
    else:
        print("Wrong Input")

print("\n\t\tThank you for using Calculator")

