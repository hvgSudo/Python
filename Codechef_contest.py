a = int(input())
for i in range(a):
    if (i > 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
