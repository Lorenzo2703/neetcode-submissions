import random


class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = []
        self.weight = 0

        for i in w:
            self.weight += i
            self.prefix.append(self.weight)

    def pickIndex(self) -> int:
        rand = random.randint(1, self.weight)

        low=0
        high=len(self.prefix)-1

        while low < high:
            mid = (low+high)//2
            
            if rand <= self.prefix[mid]:
                high=mid
            else:
                low=mid+1

        return low


