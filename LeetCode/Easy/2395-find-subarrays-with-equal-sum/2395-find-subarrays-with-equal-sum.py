class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        store = set()
        for i in range(len(nums)-1):
            s = nums[i] + nums[i+1]
            if s in store:
                return True
            
            store.add(s)
        
        return False