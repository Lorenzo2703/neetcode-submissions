class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        sets = set()

        for i in range(len(s)):

            while s[i] in sets:
                sets.remove(s[left])
                left+=1

            sets.add(s[i])
            longest = max(longest,i-left+1)

        
        return longest
        
            
        