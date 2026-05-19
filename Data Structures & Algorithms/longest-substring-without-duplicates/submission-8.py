class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = {}
        max_length = 0
        start = 0

        for i,n in enumerate(s):
            if n in char_set and char_set[n]>=start:
                start=char_set[n]+1
                
            char_set[n]=i
            max_length= max(max_length,i-start+1)

        return max_length