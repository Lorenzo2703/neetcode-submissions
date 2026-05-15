class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        lista = [1]*length

        prefix = 1
        for i in range(length):
            lista[i]=prefix
            prefix *= nums[i]

        suffix=1
        for i in range(length-1,-1,-1):
            lista[i]*=suffix
            suffix*=nums[i]
        

        print(lista)
        return lista
        