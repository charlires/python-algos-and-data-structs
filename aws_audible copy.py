from typing import List, Set

class Solution: 
    # every iteration check that position to find relationships
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        def dfs(i):
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    visited.add(j)
                    dfs(j)
        
        visited = set() 
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                dfs(i)
        
        return res
                
    
# matrix = [
#     [1, 1, 0, 0],
#     [1, 1, 1, 0],
#     [0, 1, 1, 0],
#     [0, 0, 0, 1]
# ]
# print(Solution().findCircleNum(matrix))
# matrix = [
#     [1, 1, 0, 0],
#     [1, 1, 0, 1],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1]
# ]
# print(Solution().findCircleNum(matrix))
matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 1]
]
print(Solution().findCircleNum(matrix))

