number = int(input("Enter a non floating point number: "))

binary = list()

while number > 0:
    binary.append(number % 2)
    number = number // 2

binary.reverse()

for i in binary:
    print(i, end="")
print()