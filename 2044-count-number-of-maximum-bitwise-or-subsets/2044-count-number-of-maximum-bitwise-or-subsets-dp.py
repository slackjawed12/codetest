class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx_or = 0
        for n in nums:
            mx_or = mx_or | n
        
        result = []
        def back(nums, idx, cur, val):
            if val == mx_or:
                result.append(cur[:])
            
            for i in range(idx+1,len(nums)):
                cur.append(nums[i])
                back(nums, i, cur, nums[i] | val)
                cur.pop()
        
        back(nums, -1, [], 0)
            
        return len(result)