m = int(input('number of rows, m : '))
n = int(input('number of columns, n : '))
a=[]
for i in range(1,m+1):
  b = []
  print("{0} Row".format(i))
  for j in range(1,n+1):
    b.append(int(input("{0} Column: " .format(j))))
  a.append(b)
print(a)
