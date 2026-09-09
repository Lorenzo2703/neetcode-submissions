class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n_3=len(nums)//3

        return [x for x, count in Counter(nums).items() if count > n_3]