from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = deque([0, 1, 1])
        for _ in range(3, n+1):
            dp.append(dp[-1]+dp[-2]+dp[-3])
        
        return dp[n]