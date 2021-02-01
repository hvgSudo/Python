import datetime
a = input("Enter the date in the format YYYY-MM-DD: ")
y, m, d = map(int, a.split('-'))
a = datetime.date(y, m, d)
b = datetime.date.today()
if a == b:
    print("The date is correct")
    c = d + 1
    d = datetime.date(y, m, c)
    print("Tomorrow's date is ",d)
else:
    print("The date is wrong")
    print("The today's date is ",b)