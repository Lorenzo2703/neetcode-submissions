class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def backtrack(sums, i):
            # Base cases
            if sums == amount:
                return 1
            if sums > amount or i == len(coins):
                return 0
            
            # Check memoization using the state (sums, i)
            if (sums, i) in memo:
                return memo[(sums, i)]

            # Choice 1: Include the current coin (we can reuse it, so index remains `i`)
            include = backtrack(sums + coins[i], i)
            
            # Choice 2: Skip the current coin and move to the next index `i + 1`
            skip = backtrack(sums, i + 1)

            # Store the total valid ways for this state
            memo[(sums, i)] = include + skip
            return memo[(sums, i)]

        return backtrack(0, 0)