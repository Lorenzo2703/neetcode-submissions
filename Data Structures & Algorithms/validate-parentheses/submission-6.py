class Solution:
    def isValid(self, s: str) -> bool:
        # s can be empty?
        # Time Complexity O(n), Space Complexity O(n)

        stack = []

        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                pop = stack.pop()
                if (
                    (pop == "{" and i != "}")
                    or (pop == "[" and i != "]")
                    or (pop == "(" and i != ")")
                ):
                    return False

        return True if not stack else False
