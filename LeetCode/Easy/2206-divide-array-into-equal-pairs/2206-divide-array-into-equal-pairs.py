class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        store = {}
        for num in nums:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1
        
        for count in store.values():
            if count % 2 != 0:
                return False
                
        return True

        