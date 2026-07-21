class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # If there are only 2 steps, the cheapest is just the minimum of the two
        if n <= 2:
            return min(cost)

        # Build up the minimum cost to reach each step
        # We start by iterating from index 2 up to the end of the stairs
        for i in range(2, n):
            # To get to step i, you must have come from i-1 or i-2. 
            # Add the minimum of those previous two choices to the current step.
            cost[i] += min(cost[i - 1], cost[i - 2])

        # The top of the stairs can be reached from either of the last two steps
        return min(cost[-1], cost[-2])