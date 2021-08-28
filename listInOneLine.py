even = [i for i in range(10) if i % 2 == 0]
print("Even:", even)

a = [i for i in range(10)]
even1 = list(filter(lambda x : x % 2 == 0, a))
print("Even using lambda:", even1)