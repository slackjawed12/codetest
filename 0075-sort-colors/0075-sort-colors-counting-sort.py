class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one = 0, 0
        for n in nums:
            if n == 0:
                zero += 1
            elif n == 1:
                one += 1
        
        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif zero <= i < zero+one:
                nums[i] = 1
            else:
                nums[i] = 2
