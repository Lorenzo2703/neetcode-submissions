class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}

        for i in range(len(strs)):
            sortedword = "".join(sorted(strs[i]))
            answer.setdefault(sortedword,[]).append(strs[i])
        return list(answer.values())
