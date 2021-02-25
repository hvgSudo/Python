file = open("D:\\Downloads\\a.txt", "r")
lst = B = E = Names = L = list()
dct = dict()
count = 0

firstLine = file.readline()
lst.append(firstLine.split(" "))
D = int(lst[0][0]) # time given
I = int(lst[0][1]) # intersection points
S = int(lst[0][2]) # number of streets
V = int(lst[0][3]) # Cars
F = int(lst[0][4]) # Score for each car

while(True):
    count = count + 1
    currentLine = file.readline()
    if (not currentLine):
        break
    lst.append(currentLine.split(" "))
    # [[B, E, Names, L], [], []]

for i in lst:
    print(i)