class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(current_path):
            # Base case: se la lunghezza del percorso è uguale a quella dei nums, abbiamo una permutazione
            if len(current_path) == len(nums):
                # Importante: .append() passa un riferimento, quindi usiamo .copy()
                result.append(current_path.copy())
                return
            
            for num in nums:
                # Constraint: non usare numeri già presenti nel percorso attuale
                if num in current_path:
                    continue
                
                # Make choice
                current_path.append(num)
                
                # Backtrack
                backtrack(current_path)
                
                # Undo choice
                current_path.pop()
        
        backtrack([])
        return result