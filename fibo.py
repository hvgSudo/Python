def fib(a):
    b , c = 0 , 1

    while b < a:
        print(b,end=' ')
        b , c = c , b + c
