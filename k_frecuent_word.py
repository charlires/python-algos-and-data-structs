from typing import List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        m = {}
        for i in words:
            if i not in m: 
                m[i] = 0
            m[i] += 1

        heap = []
        for i in m.keys(): 
            heapq.heappush(heap, (m[i], i))

        return list(map(lambda x: x[1], heapq.nlargest(k, heap)))

print(Solution().topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
    