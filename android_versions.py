
# In Android (the popular Google mobile operating system), the executable files storing apps on devices are called "APKs". And each APK contains something called a "Manifest" which stores which devices it is compatible with. So for example, it might say needs a specific Android version, or needs a GPS chip. In this question, we are only going to think about the Android version requirements in the Manifest.

# There are two values minSDKVersion and maxSDKVersion. Each of these is optional, and inclusive. By this I mean APKs don't have to specify minSDKVersion, but if they specify minSDKVersion = 3, then Android versions 3,4,5,etc all match, but 1 and 2 don't.

# An app developer can upload multiple APKs for their app to the Play Store, each with a different manifest. For example, they might have three APKs:

# APK	    Min SDK Version	  Max SDK Version
# APK A	    4	              -
# APK B	    0	              16
# APK C	    7	              10
# Now, on Google Play you can have more than one APK per App, and we need to decide which one to deliver. So you could have A,B, and C. As part of this process we need to split up the space of all phones to which APKs they match.

# We want to divide the integer list of SDK versions into intervals that match the same APKs. So for this set we want to produce:

# (0-3), (4-6), (7-10), (11-16), (>=17)

# This is because <=3 matches only APK B, then (4-6) matches APK A & B, but not C, etc.

# Use whatever sensible data structure you want to represent the input and the output.
  

# input = [[4, MAX],[MIN, 16],[7, 10]]

# input = [(0, True), (4, True), (7, True), (10, False), (16, False), (100, False)]

# len(input) = 6 - 1 = 5 
# i = 5
# input[i] = (16, False)
# input[i+1] = (100, False)
# l = 17
# r = 100

# output = [(0-3), (4-6), (7-10), (11-16), (17, 100)]
# 
from typing import List, Tuple
def versionIntervals(input: List[Tuple]) -> List[Tuple]:
  i = 0
  result = []
  while i < len(input) - 1:
    l = 0
    r = 0 
    if input[i][1]:
        l = input[i][0]
    else: 
        l = input[i][0] + 1
    if input[i+1][1]:
        r = input[i+1][0] -1
    else:
        r = input[i+1][0]
    result.append((l, r))
    i += 1
  return result

print(versionIntervals([(0, True), (4, True), (7, True), (10, False), (16, False), (100, False)]))
  
  
# # prod improvements
# ## performance
# - cache using the input as key

# ## security
# - validate input
# - avoid negative numbers
# - make sure the version is valid and with in range


# Time Complexity: O(n)
  
  


# 0 - 3, 4- 6, 7- 10, 

# [0, 4, 7, 10, 16, MAX]

