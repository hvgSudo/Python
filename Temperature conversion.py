print("Temperature conversion")
a = int(input("1. Celsius to Fahrenheit"))
b = int(input("2. fahrenheit to Celsius"))
if a == 1:
    c = float(input("Enter temperature in Celsius: "))
    print(c," in Fahrenheit is ",((9 * c) / 5) + 32)
elif b == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f," in Celsius is ",((f - 32) * 5) / 9)
else:
    print("You IDIOT can't you give the correct output")