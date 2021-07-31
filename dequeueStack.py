from collections import deque

# stack using dequeue
numbers = deque()

print("Numbers dequeue Stack -> ", numbers)
numbers.append(23)
print("Numbers dequeue Stack -> ", numbers)
numbers.append(45)
print("Numbers dequeue Stack -> ", numbers)
numbers.append(12)
print("Numbers dequeue Stack -> ", numbers)
numbers.append(54)

print("Numbers dequeue Stack -> ", numbers)

print(numbers.pop())
print("Numbers dequeue Stack -> ", numbers)
print(numbers.pop())
print("Numbers dequeue Stack -> ", numbers)
print(numbers.pop())
print("Numbers dequeue Stack -> ", numbers)