a = {0,1,2,3,4,6,7,8,9}
b = {9,7,5,3,1,0}
print("a = ",a)
print("b = ",b)
print("Intersection of two sets")
for i in a:
    for j in b:
        if i == j:
            print(j)
print("Union of two sets")
print(a.union(b))