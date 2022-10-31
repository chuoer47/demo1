class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        dp = [[False]*(lp+1) for _ in range(ls+1)]
        dp[0][0] = True
        for i in range(ls+1):
            for j in range(1, lp+1):
                if p[j-1] == "*":
                    dp[i][j] |= dp[i][j-2]
                    if matches(i, j-1):
                        dp[i][j] |= dp[i-1][j]
                else:
                    if matches(i, j):
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        return dp[ls][lp]



s = ""
p = "a*"
res = Solution()
print(res.isMatch(s, p))
