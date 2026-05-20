class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = {}
        start = 0
        length = 0

        for i in range(len(s)):
            charset[s[i]] = charset.get(s[i], 0) + 1

            if (i - start + 1) - max(charset.values()) > k:
                charset[s[start]] -= 1
                start += 1

            length = max(length, i - start + 1)

        print(charset)
        return length
