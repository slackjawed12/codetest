class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            if num % 3 == 0:
                continue

            if (num+1) % 3 == 0:
                result += 1
            elif (num-1) % 3 == 0:
                result += 1
        
        return result
