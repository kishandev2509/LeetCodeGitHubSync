class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        visited = [False] * len(baskets)
        unplaced = 0
        for fruit in fruits:
            placed = False
            for i in range(len(baskets)):
                if not visited[i] and baskets[i] >= fruit:
                    visited[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced