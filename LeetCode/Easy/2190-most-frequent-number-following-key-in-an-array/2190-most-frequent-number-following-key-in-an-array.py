from collections import defaultdict

class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        counter= defaultdict(int)
        for i in range(len(nums)-1):
            if nums[i] == key:
                counter[nums[i+1]] += 1
        
        mc = -1
        result = -1
        for k,v in counter.items():
            if mc < v:
                mc = v
                result = k

        return result