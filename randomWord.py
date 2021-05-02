import random

characters = 'itsrees'
n = len(characters)
for i in range(n*10):
    print(''.join(random.choices(characters, k = n)))