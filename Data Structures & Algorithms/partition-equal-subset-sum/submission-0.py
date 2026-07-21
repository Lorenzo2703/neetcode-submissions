class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        # Start with a set containing 0 (we can always make a sum of 0 with an empty subset)
        possible_sums = {0}

        for num in nums:
            # For every number, create a new set of sums by adding this number
            # to all the sums we could already make
            new_sums = set()
            for s in possible_sums:
                new_sums.add(s + num)
                new_sums.add(s)  # keep the old sums too

            possible_sums = new_sums

            # If we've already found our target sum, we can stop early!
            if target in possible_sums:
                return True

        return target in possible_sums
