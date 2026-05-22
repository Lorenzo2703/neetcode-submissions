from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            
            # Caso 1: La metà sinistra è ordinata normalmente
            if nums[l] <= nums[m]:
                # Il target si trova all'interno della metà sinistra ordinata?
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Stringiamo a sinistra
                else:
                    l = m + 1  # Esploriamo la destra
                    
            # Caso 2: La metà destra è ordinata normalmente
            else:
                # Il target si trova all'interno della metà destra ordinata?
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Stringiamo a destra
                else:
                    r = m - 1  # Esploriamo la sinistra
                    
        return -1