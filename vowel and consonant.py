a = input("Enter the word: ")
b = a.lower()
e = 0
d = 0
c = "abcdefghijklmnopqrstuvwxyz"
for i in b:
    for j in c:
        if i == j:
            d = d + 1
        else:
            e = e + 1
print("Number of vowels: ",d)
print("Number of consonants: ",e)