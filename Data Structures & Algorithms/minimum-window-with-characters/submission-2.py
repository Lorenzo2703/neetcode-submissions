class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        chars = {}
        chars_t = {}

        have = 0
        res,res_length = [], float("infinity")
        left = 0

        for i in t:
            chars_t[i] = chars_t.get(i, 0) + 1
        need = len(chars_t)

        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i], 0) + 1
        
            if s[i] in chars_t and chars[s[i]]==chars_t[s[i]]:
                have+=1
                
            while have == need:
                if (i - left + 1) < res_length:
                    res_length=(i - left + 1)
                    res=[left,i]
                chars[s[left]]-=1
                if s[left] in chars_t and chars[s[left]]<chars_t[s[left]]:
                    have-=1
                left+=1


        return s[res[0]:res[1]+1] if res_length != float("infinity") else ""
