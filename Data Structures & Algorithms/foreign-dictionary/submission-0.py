from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Initialize graph with all unique characters
        adj = {c: set() for word in words for c in word}
        in_degree = {c: 0 for c in adj}
        
        # 2. Build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            # Edge Case: Check for prefix violation (e.g., "abc", "ab")
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
                
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        
        # 3. Topological Sort (Kahn's Algorithm)
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        
        while queue:
            char = queue.popleft()
            res.append(char)
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. Check for cycles
        if len(res) < len(in_degree):
            return ""
            
        return "".join(res)