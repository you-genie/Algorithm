class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [None for _ in range(n+1)]

        for i in range(n+1):
            if i < 2:
                stairs[i] = 1
            else:
                stairs[i] = stairs[i-1] + stairs[i-2]

        return stairs[n]
