fname = input("Enter file: ")
fhand = open(fname)
count = dict()

for line in fhand :
    line = line.rstrip()
    words = line.split()
    for word in words :
        count[word] = count.get(word, 0) + 1

lst = list()
for k, v in count.items() :
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for v, k in lst[:10] :
    print(k, v)

print( sorted( [ (v,k) for k, v in count.items() ] ) )
