class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        length = len(s)
        if length == 0:
            return 0
        else:
            res = 0
            i = j = 0
            while i != length:
                if s[i] not in check:
                    check.add(s[i])
                else:
                    res = max(res, i-j)
                    while s[i] in check:
                        check.remove(s[j])
                        j = j+1
                    check.add(s[i])
                i = i+1
            res = max(res, i-j)
            return res

s = Solution()
result = s.lengthOfLongestSubstring("dvdf")
print(result)

# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 91.22%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 66.04%
# 的用户
# 通过测试用例：
# 987 / 987