class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Use memoization to store results of previously checked substrings
        memo = {}

        def dfs(target: str) -> bool:
            # Base case: if the string is empty, we have successfully segmented it
            if not target:
                return True
            
            # Return cached result if already calculated
            if target in memo:
                return memo[target]
            
            # Try every word in the dictionary
            for word in wordDict:
                # If the current target starts with the word
                if target.startswith(word):
                    # Recurse on the remainder of the string
                    if dfs(target[len(word):]):
                        memo[target] = True
                        return True
            
            # If no words lead to a solution, cache False
            memo[target] = False
            return False

        return dfs(s)