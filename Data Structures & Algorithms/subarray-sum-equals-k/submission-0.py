class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        res, curSum = 0, 0

        for i in nums:
            curSum+=i
            diff= curSum-k
            res+=hashmap.get(diff,0)
            hashmap[curSum]=hashmap.get(curSum,0)+1


        return res
