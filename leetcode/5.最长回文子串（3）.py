class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        n = len(s)
        # 计算臂长的函数
        def arm(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return (right-left-2)//2
        begin, end = 0, -1
        arm_len = []   # 记录每一步的臂长
        page = -1     # 代表中心点
        right = -1    # 代表最远的臂
        # i从0到n-1，计算臂长
        for i in range(n):
            if right >= i:
                i_sym = 2*page - i     # 相当于i对称的j
                min_arm_len = min(right-i, arm_len[i_sym])
                cur_arm_len = arm(i-min_arm_len, i+min_arm_len)
            else:
                cur_arm_len = arm(i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                page = i
                right = i + cur_arm_len
            if 2*cur_arm_len+1 > end-begin:
                end = i + cur_arm_len
                begin = i - cur_arm_len
        return s[begin+1:end:2]

p = Solution()
s = "aaaaa"
res = p.longestPalindrome(s)
print(res)
