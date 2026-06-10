class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset={}
        hashset2={}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashset[s[i]]= hashset.get(s[i],0)+1
            hashset2[t[i]]= hashset2.get(t[i],0)+1

        return hashset2==hashset
