class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x<0:
            flag = -1
            x = -x
        x = str(x)
        x = list(x)
        x.reverse()
        s = ""
        x = int(s.join(x))*flag
        return x if -2147483648 < x < 2147483647 else 0