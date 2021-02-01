name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
lst = list()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for w in words:
        if w == 'From':
            lst = words[1]
            count[words[1]] = count.get(words[1], 0) + 1
largest = 1
theword = None
for k, v in count.items():
        if v > largest:
            largest = v
            theword = k
print(theword, largest)
