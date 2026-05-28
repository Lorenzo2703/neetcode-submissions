import heapq

class MedianFinder:
    def __init__(self):
        # In Python i heapq sono solo Min-Heap. 
        # Per fare un Max-Heap, moltiplichiamo i numeri per -1.
        self.small = []  # Max-Heap (numeri piccoli)
        self.large = []  # Min-Heap (numeri grandi)

    def addNum(self, num: int) -> None:
        # 1. Spingi il numero nel Max-Heap dei "piccoli" (invertendo il segno)
        heapq.heappush(self.small, -1 * num)
        
        # 2. Bilancia il valore: assicurati che ogni elemento in small sia <= di ogni elemento in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # 3. Bilancia le dimensioni: la differenza di dimensioni tra i due heap non deve superare 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Se un heap è più grande dell'altro, il mediano è la sua radice (indice 0)
        if len(self.small) > len(self.large):
            return float(-1 * self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        
        # Se hanno la stessa dimensione, fai la media tra i due elementi in cima (indice 0)
        return (-1 * self.small[0] + self.large[0]) / 2.0