class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nn = n*2
        ans = []

        for i in range(nn):
            ans.append(nums[i%n])
        return ans