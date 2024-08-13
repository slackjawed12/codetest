class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        result = -1
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            l, r = nums1[i], nums2[j]
            if l == r:
                result = l
                break
            elif l < r:
                i += 1
            else:
                j += 1
        
        return result