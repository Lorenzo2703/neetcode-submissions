class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = {}
        max_length = 0
        start = 0

        for i in range(len(s)):
            curr = s[i]

            if curr in hashset and hashset[curr]>=start:
                start = hashset[curr]+1

            hashset[curr] = i

            max_length = max(max_length,i-start+1)
       
        return max_length
