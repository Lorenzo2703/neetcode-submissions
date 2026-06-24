class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]

        
        for i in range(m):
            dp[0][i] = 1 
    
        for j in range(n):
            dp[j][0] = 1


        for i in range(1,m):
            for j in range(1,n):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]

        print(dp)

        return dp[-1][-1]