"""
1) Third Party API
2) Wrapper for 1)


1) Third Party API:

class External:
    
    # private variables
    page_size = 10

    # public 
    def fetch_page(page_num: int) -> List[int]:
        pass

ext = External()

ext.fetch_page(0) -> [0, 1, 2 ... 9]
ext.fetch_page(1) -> [10, 11, 12 ... 19]


2) Wrapper that allows users to set the number of results they want:

class Fetcher:

    # define any data structures needed to solve the problem
    ext = External()

    def fetch(num_results: int) -> List[int]
        # you will need to call ext.fetch_page() to get data
        pass

f = Fetcher()

f.fetch(5) -> [0-4] ext.fetch_page(0) -> 10
f.fetch(5) -> [5-9]
f.fetch(20) -> [10-29]

"""
from typing import List

class External:
    
    # private variables
    page_size = 10

    # public 
    def fetch_page(self, page_num: int) -> List[int]:
        result = []
        for i in range(page_num * self.page_size, (page_num + 1) *self.page_size):
            result.append(i)
        return result

class Fetcher:

    # define any data structures needed to solve the problem
    # last_value_return = 0
    def __init__(self) -> None:
        # self.last_index  = 0
        self.cur_page = 0
        self.cache = []
        self.ext = External()

    def fetch(self, num_results: int) -> List[int]:
        # you will need to call ext.fetch_page() to get data
        # make the first call and count the returned items
        # put items in cache and store the last index

        while True:
            if len(self.cache[:num_results]) >= num_results:
                result =  self.cache[:num_results]
                self.cache = self.cache[num_results:]
                return result
            
            items = self.ext.fetch_page(self.cur_page)
            self.cur_page += 1
            self.cache.extend(items)

# ext = External()
# print(ext.fetch_page(0))
# print(ext.fetch_page(1))

# print(fetcher.fetch(5))
#  X  X  X  X  X
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

fetcher = Fetcher()
print(fetcher.fetch(5))
print(fetcher.fetch(6))
print(fetcher.fetch(20))


# Your previous Plain Text content is preserved below:

# Pad for Carlos Andonaegui - Tech Lead - Backend