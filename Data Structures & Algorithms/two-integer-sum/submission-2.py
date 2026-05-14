class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in seen:
                seen[difference] = i
            if nums[i] in seen and seen[nums[i]] !=i:
                return [seen[nums[i]],i]

        print(seen)