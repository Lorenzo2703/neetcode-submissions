class TimeMap:
    def __init__(self):
        # Usiamo un dizionario dove ogni chiave punta a una lista di [timestamp, value]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        res = ""
        
        # Ricerca binaria manuale
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid][0] <= timestamp:
                # Se questo timestamp è valido, potrebbe essere la risposta migliore
                # ma cerchiamo se ce n'è uno più grande (più vicino al target)
                res = arr[mid][1]
                left = mid + 1
            else:
                # Il timestamp è troppo grande, dobbiamo cercare a sinistra
                right = mid - 1
        
        return res