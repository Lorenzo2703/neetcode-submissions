class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2: return False
        
        # Sort s1 once to have a reference
        target = sorted(s1)
        
        # Slide a window across s2
        for i in range(n2 - n1 + 1):
            # Take the current window of size n1
            window = s2[i : i + n1]
            
            # If the sorted window matches the sorted s1, it's a permutation
            if sorted(window) == target:
                return True
                
        return False