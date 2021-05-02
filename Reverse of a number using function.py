def rev(a):
    rn = 0
    while a > 0:
        r = a % 10
        rn = rn * 10 + r
        a = a // 10
    print("The reversed number is: ",rn)

a = int(input("Enter the number to be reversed: "))
rev(a)
