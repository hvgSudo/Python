def fact(a):
    i = 1
    while a > 0:
        i = i * a
        a = a - 1
    return(i)

while 1 == 1:
    print("\n1. Factorial")
    print("2. Quit")
    b = input("Enter your choice: ")

    try:
        b = int(b)
    except:
        print("\nInvalid input, only numbers accepted")
        continue
    
    if b == 1:
        a = int(input("\nEnter a number: "))
        print("\nFactorial of",a,": ",fact(a))
    elif b == 2:
        break
    else:
        print("Wrong Input")

print("\n\t\tThank You for Using Factorial")
