class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        m = {}
        def timeToInt(time: str) -> int:
            t = x.split(":")

            h = int(t[0]) * 60
            if x == "00": 
                h = 24 * 60

            m = int(t[1])
            return h + m

        for i, x in enumerate(timePoints):
            if x in m: 
                continue
            m[x] = timeToInt(x)

        res = 100000000000000000000
        for i in range(len(timePoints)-1):
            for j in range(i+1, len(timePoints)):
                res = min(res, abs(m[timePoints[i]] - m[timePoints[j]]))

        return res

print(Solution().findMinDifference(["05:31","22:08","00:35"]))