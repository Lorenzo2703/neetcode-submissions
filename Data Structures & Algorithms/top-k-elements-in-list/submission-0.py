class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for i in range(len(nums)):
            result[nums[i]] = result.get(nums[i], 0) + 1

        # Sort the dictionary keys by their values (frequencies) in descending order
        sorted_keys = sorted(result, key=result.get, reverse=True)
        return sorted_keys[:k]