class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [""] * numRows
        i = 0
        while i < len(s):
            j = 0
            while j < numRows and i < len(s): 
                arr[j] += s[i]
                i += 1
                j += 1
            j = numRows -2
            while j > 0 and i < len(s):
                arr[j] += s[i]
                i += 1
                j -= 1
        return "".join(arr)
print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("PAYPALISHIRING", 4))
# assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR" 