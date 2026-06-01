class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()
        
        def backtrack(current_path):
            if len(current_path) == len(nums):
                result.append(current_path.copy())
                return
            
            for num in nums:
                # Usiamo il set 'used' per il controllo O(1)
                if num in used:
                    continue
                
                # Make choice
                used.add(num)
                current_path.append(num)
                
                # Backtrack
                backtrack(current_path)
                
                # Undo choice (rimuoviamo da entrambi!)
                current_path.pop()
                used.remove(num)
        
        backtrack([])
        return result