class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        result = 0
        for x in nums1:
            for y in nums2:
                if x % (y*k) == 0:
                    result += 1

        return result

                