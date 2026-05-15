class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(257)
        
        stringa=""
        for s in strs:
            stringa+=str(len(s)) + "#" + s
        return stringa
    

    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []
        
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        
        return res