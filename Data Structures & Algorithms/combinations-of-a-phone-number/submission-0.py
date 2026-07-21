class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(part, i):

            
            if len(part) == len(digits):
                res.append(part)
                return

            for j in digitToChar[digits[i]]:
                backtrack(part+j,i+1)

        backtrack("", 0)

        return res
            
