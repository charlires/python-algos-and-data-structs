x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = map(lambda i: i * 2, x)
# for k, v in y.: 
print(list(y))
    


# import random

# random.randrange(10) # Integer from 0 to 9 inclusive
# random.randint(0, 10) # Integer from 0 to 9 inclusive
# random.randrange(0, 101, 2)                 # Even integer from 0 to 100 inclusive
# random.choice(['win', 'lose', 'draw']) # any
# myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# random.shuffle(myArray)
# myArray # any

import collections

c = collections.Counter()
c[1]

print(10**3)

# n = 6
def counter(n):
    count = 0
    for i in range(n):
        count += i
        # for j in range(i+1, n):
        #     count += 1
    return count

def pairs(n):
    return (n * (n-1)) // 2

# print(counter(2), pairs(2))
# print(counter(3), pairs(3))
# print(counter(4), pairs(4))
# print(counter(5), pairs(5))
# print(counter(6), pairs(6))
# print(counter(7), pairs(7))
# print(counter(8), pairs(8))
# print(counter(9), pairs(9))
# print(counter(10), pairs(10))