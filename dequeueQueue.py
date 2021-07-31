from collections import deque

names = deque()

print("Names dequeue Queue -> ", names)
names.append("Radhika")
print("Names dequeue Queue -> ", names)
names.append("Shyam")
print("Names dequeue Queue -> ", names)
names.append("Ravi")
print("Names dequeue Queue -> ", names)
names.append("Shivani")

print("Names dequeue Queue -> ", names)

print(names.popleft())
print("Names dequeue Queue -> ", names)
print(names.popleft())
print("Names dequeue Queue -> ", names)