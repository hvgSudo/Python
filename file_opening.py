'''fname = input("Enter the file name: ")
fhandle = open(fname)
for line in fhandle :
    line = line.rstrip()
    print(line)'''
with open("Harsh.txt") as file:
    for i in file:
        print(i.strip())