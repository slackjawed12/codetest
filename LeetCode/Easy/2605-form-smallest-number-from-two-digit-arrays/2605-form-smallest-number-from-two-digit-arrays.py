class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        s1,s2 = set(nums1), set(nums2)
        inter = s1 & s2
        if len(inter) > 0:
            arr = list(inter)
            arr.sort()
            return arr[0]

        nums1.sort()
        nums2.sort()
        l, h = min(nums1[0], nums2[0]), max(nums1[0], nums2[0])
        return l*10+h
       