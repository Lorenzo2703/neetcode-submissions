class Solution:
    def __init__(self, w: List[int]):
        # 1. Creiamo le nostre "soglie" (prefix sums)
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total = total

    def pickIndex(self) -> int:
        # 2. Lanciamo il dardo (numero casuale)
        import random
        target = random.randint(1, self.total)
        
        # 3. Cerchiamo a quale scatola appartiene (Ricerca Binaria Manuale)
        low = 0
        high = len(self.prefix_sums) - 1
        
        while low < high:
            mid = (low + high) // 2
            if target <= self.prefix_sums[mid]:
                high = mid # Il dardo è caduto a sinistra o qui
            else:
                low = mid + 1 # Il dardo è caduto a destra
        
        return low