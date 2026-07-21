class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(i):
            # Base Case: If we've reached the end of the string, 
            # we found a valid partition of palindromes.
            if i == len(s):
                res.append(path.copy())
                return

            # Try every possible end index 'j' for the current substring s[i:j+1]
            for j in range(i, len(s)):
                substring = s[i:j+1]
                
                # Only explore further if the current substring is a palindrome
                if substring == substring[::-1]:
                    path.append(substring)       # Choose
                    backtrack(j + 1)             # Explore the rest of the string
                    path.pop()                   # Unchoose (Backtrack)

        backtrack(0)
        return res