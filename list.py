n = int(input())
a = input().split(' ')
x = None
b = set(a)
b.remove(max(b))
print(max(b))
