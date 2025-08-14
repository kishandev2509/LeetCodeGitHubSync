class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            triple_digit_str = str(digit) * 3
            if triple_digit_str in num:
                return triple_digit_str
        return ""