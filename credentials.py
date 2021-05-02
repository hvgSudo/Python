def new():

    print("Enter the credentials\n")
    c_name = input("Enter the bank name on the card: ")
    c_num = input("Enter the card number: ")
    c_nam = input("Enter the first name mentioned on the card: ")
    c_expm = input("Enter the expiry month of the card: ")
    c_expy = input("Enter the expiry year of the card: ")
    c_cvv = input("Enter the CVV(3 digit number mentioned at the back of the card): ")
    c_balance = input("Enter the balance in the account: ")
    password = input("Enter the password for your file: ")
    pin = input("Enter your PIN: ")
    
    f = open(c_nam+".txt", "w+")
    
    f.write(password)
    f.write("\n")
    f.write(pin)
    f.write("\n")
    f.write("Balance: ")
    f.write(c_balance)
    f.write("\n")
    f.write("Bank Name: ")
    f.write(c_name)
    f.write("\n")
    f.write("Card Number: ")
    f.write(c_num)
    f.write("\n")
    f.write("Expiry: ")
    f.write(c_expm)
    f.write("-")
    f.write(c_expy)
    f.write("\n")
    f.write("CVV: ")
    f.write(c_cvv)
    
    f.close()
    
    return(c_nam)

def update(a, n):
    j = 0
    f = open(n+".txt", "w+")
    while 1 == 1:
        b = f.readline()
        c = b.split(1,7)
        for i in range(7):
            if c == ['B','a','l','a','n','c','e',':',' ']:
                f.write("Balance: ")
                f.write("\n")
                f.write(a)
                j = 4
                break
        if j == 4:
            break
    f.close()
    return 1