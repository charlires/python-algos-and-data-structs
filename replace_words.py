from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        # iterate over the dictionary
        # iterate over the words in the sentence
        # compate the first and last letter of the dictionary word
            # if match then check all the word and replace it

        result = sentence.split(" ")
        for root in dictionary:
            l = len(root)
            for i in range(len(result)):
                r = result[i][:l]
                if root == result[i][:l]:
                    result[i] = root
        return " ".join(result)
    
print(Solution().replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))