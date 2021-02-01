'''Stable Marriage Problem based on Gale Shapley Algorithm.
   Number of boys and girls is 4 each'''
n, c = 4, 0
lst = lst_1 = list()
for i in range(2 * n):
    if i < n:
        for j in range(n):
            print("\n\t", j + 1, "preference for", j, "from 4, 5, 6, 7: ")
            a = int(input())
            lst_1.append(a)
    else:
        for j in range(n):
            print("\n\t", j + 1, "preference for", j + n, "from 0, 1, 2, 3: ")
            a = int(input())
            lst_1.append(a)
    lst.append(lst_1)
for i in lst:
    c = c + 1
    if c % 4 == 0:
        print()
    print(i, end=' ')
