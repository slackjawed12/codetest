# simple version
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([n*n for n in nums])

# Two pointers
class Solution2:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        low, high = 0, len(nums) - 1
        result = [] 
        while low <= high:
            lsq, hsq = nums[low] * nums[low], nums[high] * nums[high]
            if lsq >= hsq:
                result.append(lsq)
                low += 1
            else:
                result.append(hsq)
                high -= 1

        result.reverse()
        return result