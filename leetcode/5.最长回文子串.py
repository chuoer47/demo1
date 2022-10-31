# 中心扩散法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expendAroundCenter(left, right):
            while left >= 0 and right <= n-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1
        begin, end = 0, 0
        for i in range(n-1):
            left1, right1 = expendAroundCenter(i, i)
            left2, right2 = expendAroundCenter(i, i+1)
            if right1 - left1 > end - begin:
                begin = left1
                end = right1
            if right2 - left2 > end - begin:
                begin = left2
                end = right2
        return s[begin:end+1]

p = Solution()
s = "ccc"
res = p.longestPalindrome(s)
print(res)






