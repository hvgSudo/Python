import credentials
print("\t\t\t\tATM")   
i = j = 0
a = input("Enter your file name: ")

f = open(a+".txt","r")
b = f.readline()
l = f.readline()
f.close()

while j < 2:
    file = input("Do you have a file with us (Y/N): ").lower()
    pin = input("Enter your file PIN: ")
    password = input("Enter your file password: ")
    if file == 'y':
        while i < 2:
            if b == password:
                if l == pin:
                    fi = open(a+".txt","r")
                    while 1 == 1:
                        w = fi.readline()
                        if w == "Balance: ":
                            print(fi.read())
                            break
                    fi.close()
                    break
            elif i == 1:
                print("Wrong Password. Try again")
            else:
                print("You have exceeded the limit to open your file")
                j = 2
            i = i + 1
    else:
        print("Create your file to access your account")
        c = credentials.new()
        print("Your file name is ", c)
        j = 2

print("\n\t\t Welcome ", c)    
print("\t What do you want to do")
print("\t 1. Withdrawal")
print("\t 2. Balance Enquiry")
print("\t 3. PIN Generation")
print("\t 4. Transfer")
print("\t 5. Deposit")
print("\n 6. Print receipt")
e = int(input())

if e == 1:
    p = input("Enter your PIN: ")
    q = input("Enter the amount you want to withdraw: ")
    r = credentials.uptdate(q,c)
    if r == 1:
        print("Please collect your money")
        print("\n")
        print("\t Mini Statement")
        while 1 == 1:
            w = f.readline()
            v = w.split(1,7)
            if v == ['B','a','l','a','n','c','e',':',' ']:
                print(f.read())
                break
        print("Thank you! Please visit again")

elif e == 2:
    p = input("Enter your PIN: ")
    fr = open(c+".txt", "r")
    for i in range(3):
        x = fr.readline()
        if i == 2:
            print(x)
            break
    print("Thank You")
    
#elif e == 3:

#elif e == 4:

#elif e == 5: