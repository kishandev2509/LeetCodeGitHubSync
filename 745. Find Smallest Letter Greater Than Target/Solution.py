class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target:
            return letters[0]
        left, right = 0, len(letters)-1
        while left < right:
            mid = left + (right - left)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left]
        