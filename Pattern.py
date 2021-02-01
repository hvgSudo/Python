def p1(n):
    for i in range(0,n):
        for j in range(0,i + 1):
            print("* ",end = "")
        print("\r")

n = 5
p1(n)

def p2(n):
    m = []
    for i in range(1,n+1):
        m.append("* "*i)
    print("\n".join(m))

n = 5
p2(n)

def p3(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

n = 5
p3(n)
