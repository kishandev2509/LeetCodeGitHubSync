class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1_000_000_007
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def power(a: int, n: int) -> int:
            ans = 1
            while n > 0:
                ans = ans * a
                n = n - 1
            return ans

        def find_ways(rem: int, cur: int, pow: int, memo: list[list[int]]) -> int:
            if rem == 0:
                return 1
            if rem < 1:
                return 0
            num = power(cur, pow)
            if num > n:
                return 0
            if memo[rem][cur] != -1:
                return memo[rem][cur]
            pick = find_ways(rem - num, cur + 1, pow, memo) % MOD
            not_pick = find_ways(rem, cur + 1, pow, memo) % MOD
            memo[rem][cur] = (pick + not_pick) % MOD
            return memo[rem][cur]

        return find_ways(n, 1, x, memo)