fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    t = line.split()
    if len(t) < 3 or t[0] != 'From':
        continue
    print(t[1])
    count = count + 1
print("There were",count,"lines in the file with From as the first word")
