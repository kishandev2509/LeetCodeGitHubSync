class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            while nums[right] == val and right > left:
                right -= 1
            if left == right and nums[left] == val:
                return left
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
        return left