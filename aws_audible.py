from typing import List, Set

class Solution: 
    # every iteration check that position to find relationships
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        groups: List[Set[int]] = []

        def findR(i: int, s: Set[int]) -> Set[int]:
            isConnected[i][i] = 0
            s.add(i)
            dfs(i+1, i, i, s)
            dfs(i-1, i, i, s)
            dfs(i, i+1, i, s)
            dfs(i, i-1, i, s)
            return s
        
        def dfs(i: int, j: int, x: int, s: Set[int]) -> Set[int]:
            if i < 0 or j < 0 or i == len(isConnected) or j == len(isConnected):
                return s
            
            if isConnected[i][j] == 1:
                isConnected[i][j] = 0
                if i != x: findR(i, s)
                elif j != x: findR(j, s)

            if i > x: dfs(i+1, j, x, s)
            elif i < x: dfs(i-1, j, x, s)
            elif j > x: dfs(i, j+1, x, s)
            elif j < x: dfs(i, j-1, x, s)
            return s
        
        for i in range(len(isConnected)):
            if isConnected[i][i] == 1:
                groups.append(findR(i, set()))

        return len(groups)
                
    
matrix = [
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1]
]
print(Solution().findCircleNum(matrix))
matrix = [
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
print(Solution().findCircleNum(matrix))
matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 1]
]
print(Solution().findCircleNum(matrix))

