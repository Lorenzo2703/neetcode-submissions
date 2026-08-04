class Solution:
    def isHappy(self, n: int) -> bool:
        dictionary = set()
        sums = 0

        while n !=1:
            sums = 0
            for i in str(n):
                i=int(i)
                sums += i*i
            if sums in dictionary:
                return False
            dictionary.add(sums)
            n=sums
        
        return True