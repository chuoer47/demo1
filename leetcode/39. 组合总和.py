class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        dic = {}
        # 初始化
        for i in range(1, target+1):
            dic[i] = []
        for i in range(1, target+1):
            for j in candidates:
                if i == j:
                    dic[i].append([j])
                if i > j:
                    for k in dic[i-j]:
                        x = k[:]
                        x.append(j)
                        x.sort()
                        if x not in dic[i]:
                            dic[i].append(x)
        return dic[target]


cand = [2,3,6,7]
tar = 7
S =Solution()
print(S.combinationSum(cand,tar))