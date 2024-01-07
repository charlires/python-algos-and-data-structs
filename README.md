# Python Algorithm Cheat Sheet 

- [Variables](#variables)
- [Math and numbers](#math-and-numbers)
- [Conditionals](#conditionals)
- [Arrays and Lists](#arrays-and-lists)
- [Loops](#loops)
- [Strings](#strings)
- [Queues and Stacks](#queues-and-stacks)
- [HashSet](#hashset)
- [HashMap](#hashmap)
- [OrderedDict](#ordereddict)
- [Tuples](#tuples)
- [Heaps](#heaps)
- [Functions](#functions)
- [Classes](#classes)
- [Stdin](#stdin)
- [HTTPRequests](#requests)
- [Try Catch](#try-catch)
- [Exceptions](#exceptions)

## Variables
```python
s = "name"
n = 0
n1, n2 = 1, 2.0
none = None

# casting
i = int("123") # 123
s = str(123) # "123"
```

## Math and numbers
```python
## division
max(10, 11) # 11
min(10, 11) # 10
abs(-10) # 10

# int() rounds float down
int(2.7) # 2 
int(-2.7) # -2 
5/2 # float 2.5

# // rounds down
5//2 # int 2.5 -> 2
-5//2 # int -2.5 -> -3 # HEADSUP

# % rounds down CAREFUL with negative numbers
10%3 # int 1
-10%3 # int 2 better use math.fmod(-10, 3)

# exponent
10**3 # 10*10*10 1000

# python numbers are infinite and never overflow
import math
math.fmod(10, 3) # float 1.0
math.fmod(-10, 3) # float -1.0
math.floor(10/3) # int 3.3333333333333335 -> 3
math.ceil(10/3) # int 3.3333333333333335 -> 4
math.sqrt(25) # float 5.0
math.pow(2, 3) # float 8.0

import random
random.randrange(10) # Integer from 0 to 9 inclusive
random.randint(0, 10) # Integer from 0 to 9 inclusive
random.randrange(0, 101, 2) # Even integer from 0 to 100 inclusive
random.choice(['win', 'lose', 'draw']) # any
myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(myArray)
myArray # [6, 0, 7, 4, 3, 5, 9, 8, 2, 1]
```

## Conditionals
```python
if True and False or True: 
    # true
elif "12" == 12: 
    # False
elif 12.0 == 12:
    # True
elif 12.0 is 12: 
    # False
elif 12.0 is 12.0: 
    # True
elif None is None:
    # True
else:
    print("else")
```
## Arrays and Lists
```python
myArray = [1, 2]
len(myArray) # 2

myArray = [1] * 5 # [1, 1, 1, 1, 1]
myArray = [i for i in range(5)] # [0, 1, 2, 3, 4]
myArray = [[0] * 4] * 3 # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
myArray = [[0] * 4 for i in range(3)] # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
myArray = [[0 for j in range(4)] for i in range(3)] # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

myArray = [1, 2]
myArray.append(4) # [1, 2, 4]
myArray.pop() # 4 

myArray.insert(1, 7) # [1, 7, 2, 4]
myArray[0] = 0 # [0, 7, 2, 4]

# get last index
myArray[-1] # 4

# HEADSUP 
myArray = [1, 2, 3]
myArray[4] = 1 # IndexError: list assignment index out of range
myArray[4] # IndexError: list index out of range
myArray.index(4) # ValueError: '4' is not in list
myArray.remove(4) # ValueError: '4' is not in list

# sublisting / slicing
myArray = [1, 2, 3, 4, 5, 6]
myArray[1:3] # [2, 3, 4]
myArray[2:9999] # [3, 4, 5, 6] # no IndexError

myArray = [1, 2, 3]
myArray.extend([4, 5, 6]) # [1, 2, 3, 4, 5, 6]

# sorting default to ascending (min to max)
myArray = [2, 3, 1]
myArray.sort() # [1, 2, 3]
myArray.sort(reverse=True) # [3, 2, 1]
myArray.reverse() # [3, 2, 1]

myArray = ["egg", "banana", "apple"]
myArray.sort() # ["apple", "banana", "egg"] by default sort alphabeticaly
myArray.sort(key=lambda x: len(x)) # ["egg", "apple", "banana"]

# unpacking
a, b, c = [1, 2, 3]
```

## Loops
```python
myArray = [10, 20, 30, 40]
for i in myArray: # without index
    print(i) # 10, 20, 30, 40

for i in range(len(myArray)): # with index
    print(myArray[i]) # # 10, 20, 30, 40

for i, v in enumerate(myArray): # with index and value
    print(i, v) # (0, 10), (1, 20), (2, 30), (3, 40)

for i in range(5): # from 0 to 4
    print(i) # 0, 1, 2, 3, 4

for i in range(1, 5): # from 1 to 4
    print(i) # 1, 2, 3, 4

for i in range(4, -1, -1): # from 4 to 0
    print(i) # 4, 3, 2, 1, 0

arr = [1, 2, 3, 4, 5]
for i in range(len(arr)): # from 0 to length of arr
    for j in range(len(arr)-1, i, -1): # from length of arr to i+1
        print((i, j))

for i in range(8, -1, -2): # from 8 to 0 jump -2
    print(i) # 8, 6, 4, 2, 0

n = 0
while n < 5:
    print(n) # 0, 1, 2, 3, 4
    n += 1

while True:
    print("infinite")
```

## Strings
```python
myStr = "abc"
myStr[0:2] # "ab"

# strings are inmutable
myStr += "def" # "abcdef" # this takes O(n)

# casting
int("123") + int("123") # 246
str(123) + str(123) # "123123"

# get ascii value
ord("a") # 97

# transform
",".join(["ab", "cd", "ef"]) # "ab,cd,ef"
"ab cd ef".split(" ") # ["ab", "cd", "ef"]
"  asdf\n  ".strip() # "asdf"
"apple".upper() # APPLE
"apple".lower() # apple
"apple".capitalize() # Apple
"apple".endswith("le") # True
"apple".startswith("goog") # False

# formatting
"hello {name}".format(name="carlos") # "hello carlos"
"${price:.2f}".format(price=49.356) # "$49.36" # HEADSUP rounds

```
## Queues and Stacks 
```python
from collections import deque

myStack = deque() # []
myStack.append(1) # [1]
myStack.append(2) # [1, 2]
myStack.append(3) # [1, 2, 3]
top = myStack.pop() # 3

myQueue = deque()
myQueue.append(1) # [1]
myQueue.append(2) # [1, 2]
myQueue.append(3) # [1, 2, 3]
dequeued = myQueue.popleft() # [1]

myQueue.appendleft(1) # [1, 2, 3]
```
## HashSet
```python
mySet = set()
mySet.add(1) # {1}
mySet.add(2) # {1, 2}
len(mySet) # 2
print(1 in mySet) # True
print(3 not in mySet) # True
mySet.remove(2) # {1}

mySet = set([1, 2]) # {1, 2}
mySet = set({i for i in range(3)}) # {0, 1, 2}
```
## HashMap
```python
myMap = {} # {}
myMap["key1"] = "one" # {"key1": "one"}
myMap["key2"] = 2 # {"key1": "one", "key2": 2}
len(myMap) # 2
print("key1" in myMap) # True
myMap.pop("key1") 

# HEADSUP 
myMap = {}
myMap["key3"] # KeyError: 'key3'
myMap.get("key3") # None

# Disc comprehencion
myMap = { i: i*2 for i in range(3)} # {0: 0, 1: 2, 2: 4}

# To list of keys
keys = list(myMap) # ["key1", "key2"]

# Iterate over HashMaps
myMap = {"key1": 1, "key2": 2}
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)
```

## OrderedDict
```python
from collections import OrderedDict

myOrderedMap = OrderedDict()
myOrderedMap["key1"] = 1 # {"key1": 1}
myOrderedMap["key2"] = 2 # {"key1": 1, "key2": 2}
myOrderedMap["key3"] = 3 # {"key1": 1, "key2": 2, "key3": 3}

# Stack/LIFO
myOrderedMap.move_to_end("key2", last=True) # {"key1": 1, "key3": 3, "key2": 2}
myOrderedMap.popitem(last=True) # {"key1": 1, "key3": 3}
# Queue/FIFO
myOrderedMap.move_to_end("key2", last=False) # {"key2": 2, "key1": 1, "key3": 3}
myOrderedMap.popitem(last=False) # {"key1": 1, "key3": 3}
```

## Tuples 
```python
# Tuple are like arrays but inmutables
myTuple = (1, 2, 3)
myTuple[1] # 2

# can be used as keys in maps and sets
myMap = { (1, 2): 3}
myMap[(1, 2)] # 3

mySet = set() # []
mySet.add((1, 2)) # [(1, 2)]
print((1, 2) in mySet) # True
```
## Heaps
```python
import heapq

minHeap = []
heapq.heappush(minHeap, 3) # [3]
heapq.heappush(minHeap, 2) # [2, 3]
heapq.heappush(minHeap, 4) # [2, 3, 4]
minHeap[0] # 2 min
minHeap[-1] # 4 max
# minHeap[-2] # 3 max

# # build a heap from initial values
myArray = [2, 1, 8, 4, 5]
heapq.heapify(myArray) # [1, 2, 4, 5, 8]

# iterate over heaps
while len(minHeap):
    print(heapq.heappop(minHeap)) 

# myArray = [2, 1, 8, 4, 5]

# heapq.heapify(myArray) # [1, 2, 4, 5, 8]
# while len(myArray):
#     print(heapq.heappop(myArray))

# heaps accepts tuples  
# orders them by the first value
tupleHeap = []
heapq.heappush(tupleHeap, (3, "task1")) # [(3, "task1")]
heapq.heappush(tupleHeap, (2, "task2")) # [(2, "task2"), (3, "task1")]
heapq.heappush(tupleHeap, (4, "task3")) # [(2, "task2"), (3, "task1"), (4, "task3")]
print(minHeap[0]) # (2, "task2") min
print(minHeap[-1]) # (4, "task3") max
```

## Functions
```python
def myFunc(n: int, m: int) ->  int:
    return n*m

myFunc(2, 3) # 6
```

## Classes
```python
from typing import List

class MyClass:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.size = len(nums)
    def getLength(self) -> int:
        return self.size
    
    def getDoubleLenght(self) -> int:
        return 2 * self.getLength()
    
myClass = MyClass([1, 2, 3, 4, 5, 6, 7, 8, 9])
myClass.getLength() # 9
```

## stdin
```python
# single line
i = input()

# multiline
import sys
lines = sys.stdin.readlines()

lines = [line for line in sys.stdin]

# from file
with open("myfile.txt") as f:
    lines = f.readlines()
```

## requests
```python
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
print(x.content)
print(x.headers)
```

## Try Catch
```python
try: 
    pass
except ValueError: # IndexError: KeyError:
    pass
```

## Exceptions

| Exception Name        | Possible Causes                                |
|-----------------------|-------------------------------------------------|
| SyntaxError           | Syntax errors in your code, e.g., missing colons or quotes.                  |
| IndentationError      | Issues with code indentation, like mixing spaces and tabs.                 |
| NameError            | Accessing an undefined variable or function.                                |
| TypeError             | Inappropriate operation or function on an object.                          |
| ValueError            | Function receives a correct type but inappropriate value.                  |
| KeyError              | Attempting to access a non-existent dictionary key.                        |
| IndexError            | Trying to access an index out of range in a sequence.                      |
| FileNotFoundError     | Opening or manipulating a file that doesn't exist.                         |
| ModuleNotFoundError   | Module you're trying to import can't be found.                              |
| ZeroDivisionError     | Division by zero.                                                          |
| AttributeError        | Accessing an attribute or method that doesn't exist.                        |
| ImportError           | Issues with importing, e.g., circular imports or missing dependencies.     |
| IOError               | Various I/O-related issues, like file reading or writing problems.          |
| PermissionError       | Attempting an operation without necessary permissions, e.g., writing to a read-only file. |# python-algos-and-data-structs
