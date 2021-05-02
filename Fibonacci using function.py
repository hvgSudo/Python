def fib(a):
    b , c = 0 , 1

    while b < a:
        print(b,end=' ')
        b , c = c , b + c
    

while 1 == 1:
    print("\n\n1. Fibonacci series")
    print("2. Quit")
    e = input("Enter your choice: ")

    try:
        e = int(e)
    except:
        print("\nInvalid input, only numbers accepted")
        continue

    if e == 1:
        a =int(input("\nEnter the number till where you want the series to go: "))
        print("\nThe Fibonacci Series is")
        fib(a)
    elif e == 2:
        break
    else:
        print("Wrong Input")

print("\n\t\tThank you for using Fibonacci")
