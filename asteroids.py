from collections import deque

class Solution:
    def asteroidCollision(self, asteroids) :
        if len(asteroids) <= 1:
            return asteroids
        
        stack = deque()
        while len(asteroids) > 0:
            if len(stack) == 0:
                stack.append(asteroids.pop())
            else:
                top = stack[-1]
                current = asteroids[-1]

                if top < 0 and current > 0 :
                    top = abs(top)
                    current = abs(current)

                    if top == current:
                        stack.pop()
                        asteroids.pop()

                    if top > current:
                        asteroids.pop()

                    if top < current: 
                        stack.pop()

                else:
                    stack.append(asteroids.pop())

        while len(stack) > 0:
            asteroids.append(stack.pop())

        return asteroids
    
# stack = [10]
# asteroids = []
# top = 0
# current = 10

# print(Solution().asteroidCollision([-2, -1, 1, 2]))
# print(Solution().asteroidCollision([-2,-2,-2,1]))
# print(Solution().asteroidCollision([1, -2,-2,-2]))
print(Solution().asteroidCollision([-2,-2,1,-1]))
        # i = len(asteroids) -1
        # while i > 0:
        #     as1 = asteroids[i]
        #     as2 = asteroids[i-1]
        #     if as1 < 0 and as2 > 0 :
        #         as1 = abs(as1)
        #         as2 = abs(as2)
        #         if as1 == as2:
        #             asteroids.pop(i)
        #             asteroids.pop(i-1)
        #             i -= 1
        #         if as1 > as2:
        #             asteroids.pop(i-1)
        #         if as1 < as2: 
        #             asteroids.pop(i)
        #     i -= 1
        # return asteroids
    