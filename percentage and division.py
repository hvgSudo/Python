print("Enter the marks of five subjects")
a = int(input("Enter the marks of subject 1: "))
b = int(input("Enter the marks of subject 2: "))
c = int(input("Enter the marks of subject 3: "))
d = int(input("Enter the marks of subject 4: "))
e = int(input("Enter the marks of subject 5: "))
per = (a + b + c + d + e) / 5
if per >= 90:
    print("\nThe percentage of student is: ", per)
    print("The student has secured First Division")
elif per >= 80 and per < 90:
    print("\nThe percentage of student is: ", per)
    print("The student has secured Second Division")
elif per >= 70 and per < 80:
    print("\nThe percentage of student is: ", per)
    print("The student has secured Third Division")
elif per >= 60 and per < 70:
    print("\nThe percentage of student is: ", per)
    print("The student has secured Fourth Division")
elif per >= 50 and per < 60:
    print("\nThe percentage of student is: ", per)
    print("The student has secured Fifth Division")
elif per >= 40 and per < 50:
    print("\nThe percentage of student is: ", per)
    print("The student has secured Sixth Division")
else:
    print("\nThe percentage of student is: ", per)
    print("The student has Failed")
