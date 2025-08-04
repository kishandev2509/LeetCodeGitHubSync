class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_types = {}
        total_fruits_in_basket, max_fruits = 0, 0
        left, right = 0, 0
        while right < len(fruits):
            if fruits[right] not in fruit_types:
                fruit_types[fruits[right]] = 1
                total_fruits_in_basket += 1
            else:
                fruit_types[fruits[right]] += 1
            right += 1
            while total_fruits_in_basket > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    fruit_types.pop(fruits[left])
                    total_fruits_in_basket -= 1
                left += 1
            max_fruits = max(max_fruits, right - left)
        return max_fruits
        