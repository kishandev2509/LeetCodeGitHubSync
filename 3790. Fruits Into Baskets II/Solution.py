class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        visited = [False] * n
        placed = 0
        for fruit in fruits:
            for i in range(n):
                if not visited[i] and baskets[i] >= fruit:
                    visited[i] = True
                    placed += 1
                    break
        return n - placed