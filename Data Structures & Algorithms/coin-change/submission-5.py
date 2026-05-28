class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        queue = deque([0])
        seen = set()
        steps = 0

        while queue:
            steps += 1

            for _ in range(len(queue)):
                cur = queue.popleft()

                for coin in coins:
                    if cur + coin == amount:
                        return steps
                    if cur+coin in seen or cur + coin > amount:
                        continue

                    queue.append(cur + coin)
                    seen.add(cur + coin)

        return -1
