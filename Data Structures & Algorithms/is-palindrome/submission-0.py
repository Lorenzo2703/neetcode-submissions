class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([char for char in s if char.isalnum()])
        length=len(s)

        for j in range(length):
            print(s[j],s[length-1])
            if s[j]!=s[length-1]:
                return False
            else:
                length-=1

        return True
