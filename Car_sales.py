import datetime

class car:
    def __init__(self):
        self.d = { 1 : "Mahindra Thar (10,00,000 INR)" ,
              2 : "Mahindra Scorpio (16,00,000 INR)" ,
              3 : "Mahindra Bolero (13,00,000 INR)" ,
              4 : "Ford Endeavour (26,00,000 INR)" ,
              5 : "Mahindra XUV 500 (16,00,000 INR)" ,
              6 : "Maruti Suzuki Vitara Brezza (13,00,000 INR)" ,
              7 : "Maruti Suzuki Ciaz (14,00,000 INR)" ,
              8 : "Hyundai Creta (16,00,000 INR)" ,
              9 : "Toyota Fortuner (26,00,000 INR)" ,
              10 : "Toyota Corolla Altis (25,00,000 INR)" ,
              11 : "Hyundai Fluidic Verna (16,00,000 INR)"}
        self.dr = 1

    def display(self):
        for k,v in self.d.items():
            print(k,". ",v)
    
    def sales(self,f):
        print("\n")
        for i in self.d.keys():
            if f == i:
                print(self.d[f])
        while 1 == 1:
            g = int(input("Enter your age: "))
            if g > 18:
#Personal details                
                n = input("Name of the car owner: ")
                a = input("Date of Birth in the format YYYY-MM-DD: ")
                y, m, d = map(int, a.split('-'))
                a = datetime.date(y, m, d)
                m = input("Contact number of the owner: ")
                o = input("Alternate contact number of the owner: ")
                e = input("Email ID of the owner: ")
                em = input("Alternate email ID of the owner: ")
                r = input("Aadhar number of the owner: ")
                l = input("Driving licence number of the owner: ")
                print("1. Passport")
                print("2. Voter ID")
                choose = int(input("Enter your choice: "))
                if choose == 1:
                    x = input("Passport number of the owner: ")
                    break
                elif choose == 2:
                    x = input("Voter ID number of the owner: ")
                    break
            else:
                return 0
#Confirmation of details
        while self.dr < 2:
            print("\n")
            print("\t\tConfirm your details")
            print("Name of the car owner: ",n)
            print("Date of Birth of the owner: ",a)
            print("Contact number of the owner: ",m)
            print("Alternate contact number of the owner: ",o)
            print("Email ID of the owner: ",e)
            print("Alternate email ID of the owner: ",em)
            print("Aadhar number of the owner: ",r)
            print("Driving licence number of the owner: ",l)
            if choose == 1:
                print("Passport number of the owner: ",x)
            elif choose == 2:
                print("Voter ID number of the owner: ",x)
            print("\n")
            cho = input("If the details are correct press 1 else press 0: ")
            if cho == 1:
                self.dr += 1
                break
            elif cho == 0:
                self.dr += 1
            self.dr += 1
#Transaction                
        print("\n\t\tPayment")
        print("1. Cheque")
        print("2. Credit Card")
        print("3. Debit Card")
        print("4. Loan")
        pay = int(input("How do you want to pay: "))
        if pay == 1:
            bn = input("Enter Bank name: ")
            acc = input("Enter the account number: ")
            dat = datetime.date.today()
            amount = input("Enter the amount: ")
        elif pay == 2:
            bn = input("Enter Bank name: ")
            acc = input("Enter the card number: ")
            dat = datetime.date.today()
            amount = input("Enter the amount: ")
        elif pay == 3:
            bn = input("Enter Bank name: ")
            acc = input("Enter the card number: ")
            dat = datetime.date.today()
            amount = input("Enter the amount: ")
        elif pay == 4:
            bn = input("Enter Bank name: ")
            acc = input("Enter the loan account number: ")
            DD = input("Enter the DD number: ")
            dat = datetime.date.today()
            amount = input("Enter the amount: ")
#Completion                    
        print("\n\t\t\tTransaction completed")
        print("\n\n\tCongratulations,",end = ' ')
        if f == 1:
            print("You are the owner of Mahindra Thar")
        if f == 2:
            print("You are the owner of Mahindra Scorpio")
        if f == 3:
            print("You are the owner of Mahindra Bolero")
        if f == 4:
            print("You are the owner of Ford Endeavour")
        if f == 5:
            print("You are the owner of Mahindra XUV 500")
        if f == 6:
            print("You are the owner of Maruti Suzuki Vitara Brezza")
        if f == 7:
            print("You are the owner of Maruti Suzuki Ciaz")
        if f == 8:
            print("You are the owner of Hyundai Creta")
        if f == 9:
            print("You are the owner of Toyota Fortuner")
        if f == 10:
            print("You are the owner of Toyota Corolla Altis")
        if f == 11:
            print("You are the owner of Hyundai Fluidic Verna")                
        print("\nName of the car owner: ",n)
        print("Date of Birth of the owner: ",a)
        print("Contact number of the owner: ",m)
        print("Alternate contact number of the owner: ",o)
        print("Email ID of the owner: ",e)
        print("Alternate email ID of the owner: ",em)
        print("Aadhar number of the owner: ",r)
        print("Driving licence number of the owner: ",l)
        if choose == 1:
            print("Passport number of the owner: ",x)
        elif choose == 2:
            print("Voter ID number of the owner: ",x)
        print("\n\t\t\tTransaction details\n")
        if pay == 1:
            print("Mode of payment: Cheque")
            print("Bank Name: ",bn)
            print("Paid by: ",n)
            print("Date of payment: ",dat)
            print("Amount payble: ",amount)
        elif pay == 2:
            print("Mode of payment: Credit Card")
            print("Bank Name: ",bn)
            print("Paid by: ",n)
            print("Date of payment: ",dat)
            print("Amount payble: ",amount)
        elif pay == 3:
            print("Mode of payment: Debit Card")
            print("Bank Name: ",bn)
            print("Paid by: ",n)
            print("Date of payment: ",dat)
            print("Amount payble: ",amount)
        elif pay == 4:
            print("Mode of payment: Loan")
            print("Bank Name: ",bn)
            print("Paid by: ",n)
            print("Date of payment: ",dat)
            print("Amount payble: ",amount)

r = car()  
                    
print("\n\t\tWelcome to Cars Empire\n")
r.display()
print("\n")
f = int(input("Enter the serial number of the car you want to buy: "))
w = r.sales(f)
if w == 1:
    print("\nCars Empire wishes you good life ahead with your new",r.d[f])
elif w == 0:
    print("\nYou are ineligible to buy a car")