class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            srow = set()
            scol = set()
            for j in range(9):
                cellrow = board[i][j]
                if cellrow != "." and cellrow in srow:
                    return False
                srow.add(cellrow)
                cellcol = board[j][i]
                if cellcol != "." and cellcol in scol:
                    return False
                scol.add(cellcol)
        for i in range(3):
            v = i * 3
            s1 = set()
            s2 = set()
            s3 = set()
            for j in range(3):
                j += v
                for t in range(3): 
                    cell1 = board[j][t]
                    if cell1 != "." and cell1 in s1:
                        return False
                    s1.add(cell1)
                    cell2 = board[j][t+3]
                    if cell2 != "." and cell2 in s2:
                        return False
                    s2.add(cell2)
                    cell3 = board[j][t+6]
                    if cell3 != "." and cell3 in s3:
                        return False
                    s3.add(cell3)
        return True


solution = Solution()
print(solution.isValidSudoku([
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]))
