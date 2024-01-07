class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        # send word (or word len) and a counter
        # every iteration I increase the counter to 1
        # every time I compare with the word len if we complete the word or we need to find more letters 
        # add a set and store the position every time I do deep into a search
        def findNextLetter(i, j, pos, word):
            if i == rows or i < 0 or j == cols or j < 0:
                return False

            if (i, j) in path:
                return False

            if board[i][j] != word[pos]:
                return False

            if pos == len(word)-1:
                return True
            
            path.add((i, j))

            res = (findNextLetter(i+1, j, pos+1, word) or 
                findNextLetter(i-1, j, pos+1, word) or 
                findNextLetter(i, j+1, pos+1, word) or 
                findNextLetter(i, j-1, pos+1, word))

            path.remove((i, j))
            return res

        for i in range(rows):
            for j in range(cols):
                if findNextLetter(i, j, 0, word):
                    return True
        return False

# print(Solution().exist([
#     ["A","B","C","E"],
#     ["S","F","C","S"],
#     ["A","D","E","E"]
# ], "ABCB"))
# print(Solution().exist([
#     ["A","B","C","E"],
#     ["S","F","C","S"],
#     ["A","D","E","E"]
# ], "SEE"))
# i = [1, 2, 2]
# j = [3, 3, 2]
# print(Solution().exist([
#     ["A","B","C","B"],
#     ["S","F","C","S"],
#     ["A","D","E","E"]
# ], "ABCB"))
print(Solution().exist([
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
], "ABCESEEEFS"))