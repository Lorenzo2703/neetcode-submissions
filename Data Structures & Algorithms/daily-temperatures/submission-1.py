class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack=[]

        for j,v in enumerate(temperatures):
            
            while stack and stack[-1][0]<v:
                value,index= stack.pop()
                res[index]=j-index

            stack.append((v,j))
           

        return res