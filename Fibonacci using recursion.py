def fib(a):
    if a <= 1:
        return a
    else:
        return(fib(a - 1) + fib(a - 2))

n = int(input("Enter the number: "))
i = 0
print("Fibonacci Series: \n")

for c in range(n + 1):
    print(fib(i))
    i += 1
