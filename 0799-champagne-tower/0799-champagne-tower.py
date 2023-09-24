class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (query_row + 1) for _ in range(query_row + 1)]
        dp[0][0] = poured

        for row in range(query_row):
            for glass in range(row + 1):
                excess = (dp[row][glass] - 1.0) / 2.0
                if excess > 0:
                    dp[row + 1][glass] += excess
                    dp[row + 1][glass + 1] += excess

        return min(1.0, dp[query_row][query_glass])