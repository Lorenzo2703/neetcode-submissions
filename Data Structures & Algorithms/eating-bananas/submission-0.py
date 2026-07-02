class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            target = 0
            speed = (left +right) //2
            for i in piles:
                target += math.ceil(i/speed)
            
            if target > h:
                left = speed +1
            else:
                right =speed - 1

        print(left,right)
        
        return left
