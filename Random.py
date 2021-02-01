import random
from random import randint

def ran(n):
    rs = 10**(n-1)
    rn = (10**n)-1
    return randint(rs,rn)

a = int(input("Enter the number of digits you want to generate: "))
print("The digit is: ",ran(a))

lis = []

for i in range(10):
    r = randint(1,100)
    if r not in lis:
        lis.append(r)

print("List of randomly generated 10 numbers: ",lis)

ro = random.choice(lis)

print("Random selected number from the given list: ",ro)
