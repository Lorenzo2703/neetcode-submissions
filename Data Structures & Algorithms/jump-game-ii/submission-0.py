class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # Quando raggiungiamo la fine del salto corrente
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Se la portata copre o supera l'ultimo indice, possiamo fermarci
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps