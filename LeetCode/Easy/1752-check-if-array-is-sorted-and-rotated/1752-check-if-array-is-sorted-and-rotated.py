class Solution:
    def check(self, nums: list[int]) -> bool:
       origin = sorted(nums)
       for i in range(len(nums)):
            rot = [nums[(index+i)%len(nums)] for index, num in enumerate(nums)]
            if origin == rot:
                return True
        
       return False
