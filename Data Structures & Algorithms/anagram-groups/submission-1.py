class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}

        for i in range(len(strs)):
            answer.setdefault("".join(sorted(strs[i])),[]).append(strs[i])
        return list(answer.values())
