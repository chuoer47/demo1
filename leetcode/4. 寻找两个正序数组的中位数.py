# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
#
#  
#
# 提示：
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        def findxth(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2+k-1]
                if index2 == n:
                    return nums1[index1+k-1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                newindex1 = min(index1 + k // 2 - 1, m - 1)
                newindex2 = min(index2 + k // 2 - 1, n - 1)
                if nums1[newindex1] > nums2[newindex2]:
                    k -= newindex2 - index2 + 1
                    index2 = newindex2 + 1
                else:
                    k -= newindex1 - index1 + 1
                    index1 = newindex1 + 1
        length = n+m
        if length % 2 == 1:
            return findxth(length//2 + 1)
        else:
            return (findxth(length//2)+findxth(length//2+1))/2

p = Solution()
res = p.findMedianSortedArrays([1,2],[3,4])
print(res)