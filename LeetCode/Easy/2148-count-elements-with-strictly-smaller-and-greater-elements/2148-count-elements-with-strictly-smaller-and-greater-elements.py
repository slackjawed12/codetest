from collections import defaultdict
class Solution:
    def countElements(self, nums: list[int]) -> int:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        
        sorted_list = sorted(list(set(nums)))
        result = 0
        for i in sorted_list[1:-1]:
            result += store[i]
            
        return result
            
            

class Solution2:
    def countElements(self, nums: list[int]) -> int:
        minnum, maxnum = min(nums), max(nums)
        result =0
        for num in nums:
            if num > minnum and num < maxnum:
                result += 1
            
        return result
      