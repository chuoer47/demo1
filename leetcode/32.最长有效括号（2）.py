class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [0 for _ in range(n)]
        for i in range(n):
            if s[i] == ")":
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]
                    res = max(dp[i], res)
        return res


S = Solution()
s = ")("
print(S.longestValidParentheses(s))
