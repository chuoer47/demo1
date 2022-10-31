class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        def match(x: int) -> bool:
            return s[x - 1] == '(' and s[x] == ')'

        for i in range(0, n):
            for j in range(i+1, n, 2):
                if i <= j-2:
                    dp[i][j] = dp[i][j - 2] & match(j)
                else:
                    dp[i][j] = match(j)

        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if dp[i][j]:
                    print((i, j))
                    res = max(res, j - i + 1)

        return res


S = Solution()
s = "(()()()()()()"
print(S.longestValidParentheses(s))
