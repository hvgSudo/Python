def c1():
    print("All possible combinations are")
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                print(d[i],d[j],d[k])

def c2():
    print("All possible combinations without repetition are")
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if i != j and j != k and k != i:
                    print(d[i],d[j],d[k])

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

d = []
d.append(a)
d.append(b)
d.append(c)

while 1 == 1:
    print("\n1. All Combinations")
    print("2. Combinations without repetition")
    print("3. Exit")
    e = input("Enter your choice: ")
    try:
        e = int(e)
    except:
        print("\nInvalid input, only numbers accepted")
        continue

    if e == 1:
        c1()
    elif e == 2:
        c2()
    elif e == 3:
        break
    else:
        print("\nWrong input. Try again")

print("\n\tThank you for using Combination")


