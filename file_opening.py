'''fname = input("Enter the file name: ")
fhandle = open(fname)
for line in fhandle :
    line = line.rstrip()
    print(line)'''
# with open("Harsh.txt") as file:
#    for i in file:
#        print(i.strip())

#print("Breast Cancer.names")
#with open("/mnt/d/breast-cancer.names") as f:
#    c = 0
#    for i in f:
        #if c == 5:
        #    break
#        print(i)
#        c = c + 1

print("Breast Cancer.data")
with open("/mnt/d/breast-cancer.data") as file:
    count = 0
    for i in file:
        #if count == 5:
        #    break
        print(i)
        #count = count + 1