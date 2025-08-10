class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digit(n: int) -> list[int]:
            digits = [0] * 10
            while n > 0:
                digits[n % 10] += 1
                n //= 10
            return digits

        input = count_digit(n)
        for i in range(31):
            if input == count_digit(1 << i):
                return True
        return False