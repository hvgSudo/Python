import math
print("The quadraric equation is of the form ax^2 + bx + c = 0")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = math.sqrt((b*b) - 4*a*c)
root1 = (-b + d) / 2 * a
root2 = (-b - d) / 2 * a
print("Root1: ",root1)
print("Root2: ",root2)