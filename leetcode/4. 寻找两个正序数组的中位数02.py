class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = m + n + 1
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
        left = 0
        right = m
        inf = 1000000
        median1, median2 = 0, 0
        while left <= right:
            i = (left + right)//2
            j = k//2 - i
            nums1_im1 = (-inf if i == 0 else nums1[i-1])
            nums1_i = (inf if i == m else nums1[i])
            nums2_jm1 = (-inf if j == 0 else nums2[j - 1])
            nums2_j = (inf if j == n else nums2[j])
            if nums1_im1 <= nums2_j:
                median1, median2 = max(nums1_im1, nums2_jm1), min(nums1_i, nums2_j)
                left = i+1
            else:
                right = i-1
        return (median1+median2)/2 if k%2 == 1 else median1

