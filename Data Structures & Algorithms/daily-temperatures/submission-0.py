class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Initialize the result array with 0s
        res = [0] * len(temperatures)
        stack = [] # Stores pairs of [temperature, index]

        for i, t in enumerate(temperatures):
            # While the stack is not empty AND current temp is warmer than the stack's top temp
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i # Calculate how many days you waited
                
            # Always push the current day onto the stack to wait for its warmer day
            stack.append((t, i))

        return res