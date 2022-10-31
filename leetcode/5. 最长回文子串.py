# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#  
#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
#  
#
# 提示：
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        new_s = []
        def judge(i, j) -> bool:
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        for i in range(0, n):
            for j in range(n-1, i-1, -1):
                if judge(i, j):
                    if j-i+1 > len(new_s):
                        new_s = s[i:j+1]
        return new_s

p = Solution()
s = "aacabdkacaa"
res = p.longestPalindrome(s)
print(res)