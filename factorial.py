print("Factorial of a number")
a = int(input("Enter the number: "))
i = 1
if a == 1:
    print("The factorial is 1")
else:
    while a > 0:
        i = i * a
        a = a - 1
    print("The factorial is ",i)