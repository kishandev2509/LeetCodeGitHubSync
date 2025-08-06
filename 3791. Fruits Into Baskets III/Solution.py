class Segment_Tree:
    def __init__(self, baskets) -> None:
        self.baskets = baskets
        self.tree = [0] * (len(baskets) * 4)
        self.build(0, 0, len(baskets) - 1)

    def build(self, idx, left, right):
        if left == right:
            self.tree[idx] = self.baskets[left]
            return
        mid = left + (right - left) // 2
        self.build(idx * 2 + 1, left, mid)
        self.build(idx * 2 + 2, mid + 1, right)
        self.tree[idx] = max(self.tree[idx * 2 + 1], self.tree[idx * 2 + 2])

    def is_placed(self, idx, left, right, fruit) -> bool:
        if self.tree[idx] < fruit:
            return False
        if left == right:
            self.tree[idx] = 0
            return True
        mid = left + (right - left) // 2
        if self.is_placed(idx * 2 + 1, left, mid, fruit):
            self.tree[idx] = max(self.tree[idx * 2 + 1], self.tree[idx * 2 + 2])
            return True
        if self.is_placed(idx * 2 + 2, mid + 1, right, fruit):
            self.tree[idx] = max(self.tree[idx * 2 + 1], self.tree[idx * 2 + 2])
            return True
        return False

    def __repr__(self) -> str:
        return f"{self.tree}"


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        st = Segment_Tree(baskets)
        unplaced = 0
        for fruit in fruits:
            if not st.is_placed(0, 0, len(baskets) - 1, fruit):
                unplaced += 1
        return unplaced