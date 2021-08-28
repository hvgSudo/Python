'''fname = input("Enter the file name: ")
fhandle = open(fname)
for line in fhandle :
    line = line.rstrip()
    print(line)'''
# with open("Harsh.txt") as file:
#    for i in file:
#        print(i.strip())

print("Adult.names")
with open("/mnt/d/adult.names") as f:
    c = 0
    for i in f:
        #if c == 5:
        #    break
        print(i)
        c = c + 1

print("Adult.data")
with open("/mnt/d/adult.data") as file:
    count = 0
    for i in file:
        if count == 5:
            break
        print(i)
        count = count + 1