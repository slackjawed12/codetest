class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        nums.sort()
        return self.helper(nums, 0)
    
    def helper(self, nums, result):
        if sum(nums) == 0:
            return result

        i = 0 
        while nums[i] == 0:
            i += 1

        x= nums[i]
        return self.helper([max(num-x, 0) for num in nums], result+1)
  

# we have to subtract the same amount from all elements in the array
# Elements with the same value will always take the same number of operations to become 0. 
# Contrarily, elements with different values will always take a different number of operations to become 0.
# therefore, operation count is equal to the number of unique non-zero elements in the array
class Solution2:
    def minimumOperations(self, nums: list[int]) -> int:
        return (len(set(nums)-{0}))