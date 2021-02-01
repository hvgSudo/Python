print("\n\t\tPhonebook open")
d = {}

def add():
    print("\n")
    n = input("Enter name of the person: ")
    p = input("Enter the phone number: ")
    d[n] = p
    print(d)

def rem():
    print("\n")
    n = input("Enter the name of the person: ")
    del d[n]
    print(d)

while 1 == 1:
    print("\n1. Add to the dictionary")
    print("2. Remove from the dictionary")
    print("3. Exit")
    c = int(input("Enter your choice: "))

    if c == 1:
        while 1 == 1:
            add()
            a = input("Do you want to insert more numbers (y/n): ")
            if a == 'n':
                break
    elif c == 2:
        while 1 == 1:
            rem()
            b = input("Do you want to remove more numbers (y/n): ")
            if b == 'n':
                break
    elif c == 3:
        break

print("\n\t\tPhonebook closed")
