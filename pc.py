def pco():
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
