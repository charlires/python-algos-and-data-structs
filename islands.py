class Solution:


    def numIslands(self, grid: list[list[str]]) -> int:
        # dfs 
        # recorrer la matris en busca de islas "1"
        # si encuentro una isla entonces me voy a buscar a sus alrededores si hay mas tierra "1"
        # marcar de alguna forma los pedasos de tierra que ya visite
        rows = len(grid)
        cols = len(grid[0])
        def explore(i, j):
            if i == rows or i == -1 or j == cols or j == -1:
                return
            if grid[i][j] == "1":
                grid[i][j] = "k"
                explore(i+1, j)
                explore(i-1, j)
                explore(i, j+1)
                explore(i, j-1)

        counter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    counter += 1
                    explore(i, j)

        return counter

grid = [
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["1","1","0","1","0"],
  ["0","0","1","0","0"]
]

print(Solution().numIslands(grid))
