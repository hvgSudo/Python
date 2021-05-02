file = open("D:\\Downloads\\a.txt", "r")
lst = list()
L = list()
Names, Car = list(), list()
dct = dict()
count = 0
track = 0

firstLine = file.readline()
lst.append(firstLine.split(" "))
D = int(lst[0][0]) # time given
I = int(lst[0][1]) # intersection points
S = int(lst[0][2]) # number of streets
V = int(lst[0][3]) # Cars
F = int(lst[0][4]) # Score for each car

while(True):
    currentLine = file.readline()
    if (not currentLine):
        break
    lst.append(currentLine.split(" "))
    # [[B, E, Names, L], [], []]

for i in lst:
    # print(i)
    str = i[len(i) - 1]
    i[len(i) - 1] = str.split()[0]
    # print(i)
    count = count + 1
    if (count < len(lst) and lst[count][1].isdigit()):
        # track = count
        L.append(int(lst[count][3]))
        Names.append(lst[count][2])
        # print('Count:', count)
        track = count
        # print('Track:', track)
        # print(lst[count][1])

# print()
# print(L)
# print(Names)
# print(Names.index(lst[6][1]))

for i in range(1, len(lst)):
    if (i < len(lst) - track):
        Car.append(lst[track + i])
    else:
        break

for i in Car:
    # print(i)
    sum = 0
    for j in range(1, len(i)):
        sum = sum + L[Names.index(i[j])]
    # print("Sum:", sum)
    if sum <= D:
        score = F + (D - sum)
    else:
        score = 0

# print(int(lst[1][3].split()[0]))