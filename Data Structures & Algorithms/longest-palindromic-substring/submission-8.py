class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        longest = ""
        
        # Every index is a potential center
        for i in range(len(s)):
            # 1. Odd length: Center is at i (e.g., 'aba')
            # 2. Even length: Center is between i and i+1 (e.g., 'abba')
            for center in [(i, i), (i, i + 1)]:
                left, right = center
                # Expand as long as it's a palindrome
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    # Check if this new palindrome is the longest so far
                    if (right - left + 1) > len(longest):
                        longest = s[left : right + 1]
                    left -= 1
                    right += 1
        
        return longest