class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # Slice out either the left character or the right character
                sub1 = s[l+1:r+1]
                sub2 = s[l:r]
                # Check if either remaining slice is a palindrome
                return sub1 == sub1[::-1] or sub2 == sub2[::-1]
            l, r = l + 1, r - 1
            
        return True