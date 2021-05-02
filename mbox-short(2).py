fname = input("Enter the file name: ")
fhandle = open(fname)
count = dict()
words = hours = num = result = list()

for line in fhandle :
    line = line.rstrip()
    words = line.split()
    for w in words :
        if w == 'From':
            num.append(words[5])

for i in num:
    hours = i.split(':')
    count[hours[0]] = count.get(hours[0], 0) + 1

for k, v in sorted(count.items()):
    print(k, v)
