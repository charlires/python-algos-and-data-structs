class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(p :str) -> bool:
            i = 0
            j = len(p) -1
            while i < j:
                if p[i] == p[j]:
                    i += 1
                    j -= 1
                else: 
                    return False
            return True
        
        longst = s[0:1]
        for i in range(len(s)):
            if len(longst) > len(s) - i:
                return longst
            
            for j in range(len(s)-1, i, -1):
                if s[i] == s[j] and isPalindrome(s[i:j+1]):
                    if len(longst) < len(s[i:j+1]):
                        longst = s[i:j+1]

        return longst
    
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("ab"))
# print(Solution().longestPalindrome("asdsfc"))
# print(Solution().longestPalindrome("w23asdfgfdsoiuoml"))