while 1 == 1:
    print("\n1. Prime and Composite")
    print("2. Exit")
    b = int(input("Enter your choice: "))
    j = 0
    if b == 1:
        a = int(input("\nEnter a number: "))
        if a == 1 or a == 0:
            print("\n",a," is neither a Prime nor a Composite number")
        else:
            for i in range(2,a):
                if a % i == 0:
                    print("\n",a," is a Composite number")
                    break
            else:
                print("\n",a," is a Prime number")
    elif b == 2:
        break
    else:
        print("\nWrong input")

print("\n\t\tThank you for using Prime and Composite")
