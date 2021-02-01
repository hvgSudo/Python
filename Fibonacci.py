a = int(input("Enter a number: "))
b , c = 0 , 1

print("Fibonacci Series")
while b < a:
    print(b,end=' ')
    b , c = c , b + c
    
