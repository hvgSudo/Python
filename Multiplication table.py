a = int(input("Enter the number for multilication table: "))
print("Using for loop")
for i in range(1,11):
    print(a," x ",i," = ",a * i)
print("Using While loop")
j = 1
while j < 11:
    print(a," x ",j," = ",a * j)
    j = j + 1