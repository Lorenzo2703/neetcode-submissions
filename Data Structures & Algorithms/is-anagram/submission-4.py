class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset={}
        hashset2={}

        for i in s:
            hashset[i]= hashset.get(i,0)+1

        for i in t:
            hashset2[i]= hashset2.get(i,0)+1

        return hashset2==hashset
