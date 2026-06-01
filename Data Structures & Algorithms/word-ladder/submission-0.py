from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
            
        # La coda memorizza (parola, distanza_corrente)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, dist = queue.popleft()
            
            if current_word == endWord:
                return dist
            
            # Genera le varianti con una sola lettera diversa
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + char + current_word[i+1:]
                    
                    if next_word in wordSet and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, dist + 1))
                        
        return 0