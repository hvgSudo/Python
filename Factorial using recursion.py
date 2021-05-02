def fact(a):
    i = 1
    if a == 1:
        return 1
    else:
        i = a * fact(a - 1)
    return i

a = int(input("Enter a number: "))
print("The factorial of",a,":",fact(a))
