class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] + [0] * (numRows - 1) for _ in range(numRows)]
        triangle = [[1]]
        for i in range(1, numRows):
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            triangle.append(dp[i][: i + 1])
        return triangle