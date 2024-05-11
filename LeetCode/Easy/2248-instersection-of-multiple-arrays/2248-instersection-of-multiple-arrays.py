class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
       inter = set(nums[0])
       for arr in nums[1:]:
            temp = set([])
            for num in arr:
                if num in inter:
                    temp.add(num)

            inter = temp
        
       return sorted(list(inter))