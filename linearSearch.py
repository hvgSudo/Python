a = [i for i in range(10)]

found = 0

for i in a:
    if i == 8:
        found = 1
        print("Found 8")
    
if found == 0:
    print("Element not found")