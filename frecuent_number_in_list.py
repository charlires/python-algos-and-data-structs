import heapq

def frecuent(nums: list[int], k: int) -> list[int]:
    m = {}
    for num in nums:
        if num in m:
            m[num] += 1
        else:
            m[num] = 1

    h = []
    for key, val in m.items():
        heapq.heappush(h, (-1 * val, key))
    
    return [h[i][1] for i in range(k)]

nums = [1,1,1,2,2,3]
k = 2 # return [1, 2]
print(frecuent(nums, k))

nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
k = 2 # return [1, 2]
print(frecuent(nums, k))
