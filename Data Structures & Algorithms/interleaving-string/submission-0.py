class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        memo = {}

        def dfs(i, j):
            # Base case: if we've successfully used all characters from s1 and s2
            if i == len(s1) and j == len(s2):
                return True
            
            # Check if this state has already been computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            k = i + j
            ans = False
            
            # Try matching with s1's current character
            if i < len(s1) and s1[i] == s3[k]:
                ans = ans or dfs(i + 1, j)
                
            # If not successful yet, try matching with s2's current character
            if not ans and j < len(s2) and s2[j] == s3[k]:
                ans = ans or dfs(i, j + 1)
                
            # Save the result in memo before returning
            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)