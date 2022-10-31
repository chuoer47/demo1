INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = "start"
        self.sign = 1
        self.ans = 0
        self.table = {
            "start":["start", "signed", "in_num", "end"],
            "signed":["end", "end", "in_num", "end"],
            "in_num":["end", "end", "in_num", "end"],
            "end":["end", "end", "end", "end",]
        }
    def getCol(self, c: str) -> int:
        if c == " ":
            return 0
        if c == "+" or c == "-":
            return  1
        if c.isdigit():
            return 2
        else:
            return 3
    def get(self, c):
        self.state = self.table[self.state][self.getCol(c)]
        if self.state == "in_num":
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign > 0 else min(self.ans, -1 * INT_MIN)
        if self.state == "signed":
            self.sign = 1 if c == "+" else -1

class Solution:
    def myAtoi(self, s: str) -> int:
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans

p = Solution()
s = " -42"
print(p.myAtoi(s))