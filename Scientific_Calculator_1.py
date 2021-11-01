import math

print("\n\t\t ------------ Briefing ------------\n")
print("\t Enter one of the operations given below")
print("\t Enter the second number")
print("\t +        for addition")
print("\t -        for subtraction")
print("\t *        for multiplication")
print("\t /        for division")
print("\t '%'      for remainder")
print("\t !        for factorial")
print("\t sqrt     for square root")
print("\t ^        for any power of any number")
print("\t log      for logarithm to the base 10")
print("\t ln       for natural logarithm")
print("\t g        for greatest common divisor")
print("\t sin      for sin(x)")
print("\t cos      for cos(x)")
print("\t tan      for tan(x)")
print("\t asin     for inverse sin(x)")
print("\t acos     for inverse cose(x)")
print("\t atan     for inverse tan(x)")
print("\t pi       for value of pie")
print("\t e        for value of e")
print("\t 0 to exit the calculator")
print("\nStart entering below")

while 1 == 1:
    print("\n")
    a = input("Operator: ").lower()
    
    if a == '+':
        fn = float(input())
        sn = float(input())
        print(fn ," + ", sn ," = ", fn + sn)
    
    elif a == '-':
        fn = float(input())
        sn = float(input())
        print(fn ," - ", sn ," = ", fn - sn)
    
    elif a == '*':
        fn = float(input())
        sn = float(input())
        print(fn ," * ", sn ," = ", fn * sn)
    
    elif a == '/':
        fn = float(input())
        sn = float(input())
        print(fn ," / ", sn ," = ", fn / sn)
    
    elif a == '%':
        fn = float(input())
        sn = float(input())
        print(fn ," % ", sn ," = ", fn % sn)
    
    elif a == '!':
        fn = float(input())
        print(fn ,"! = ", math.factorial(fn))
    
    elif a == 'sqrt':
        fn = float(input())
        print("Square root of ", fn ," = ", math.sqrt(fn))
    
    elif a == '^':
        fn = float(input())
        sn = float(input())
        print(fn ," ^ ", sn ," = ", math.pow(fn,sn))
    
    elif a == 'log':
        fn = float(input())
        print("log (", fn ,") = ", math.log10(fn))
    
    elif a == 'ln':
        fn = float(input())
        print("ln (", fn ,") = ", math.log(fn))
    
    elif a == 'g':
        fn = int(input())
        sn = int(input())
        print("Greatest Common Divisor of ", fn ," & ", sn ," = ", math.gcd(fn, sn))
    
    elif a == 'sin':
        fn = float(input())
        print("sin(", fn ,") = ", math.sin(fn))
    
    elif a == 'cos':
        fn = float(input())
        print("cos(", fn ,") = ", math.cos(fn))
    
    elif a == 'tan':
        fn = float(input())
        print("tan(", fn ,") = ", math.tan(fn))
    
    elif a == 'atan':
        fn = float(input())
        print("inverse tan(", fn ,") = ", math.atan(fn))
    
    elif a == 'acos':
        fn = float(input())
        print("inverse cos(", fn ,") = ", math.acos(fn))
    
    elif a == 'asine':
        fn = float(input())
        print("inverse sin(", fn ,") = ", math.asin(fn))
    
    elif a == 'pi':
        print("pi = ", math.pi)
    
    elif a == 'e':
        print("e = ", math.e)
    
    elif a == '0':
        break
    
    else:
        print("Wrong operator")

print("\n\n\t ------------ Thank You ------------")