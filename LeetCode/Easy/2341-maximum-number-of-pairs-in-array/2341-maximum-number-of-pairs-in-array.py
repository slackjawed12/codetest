class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        store = {}
        for num in nums:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1
        
        answer = [0,0]
        for num, count in store.items():
            answer[0] += count // 2
            answer[1] += count % 2
        
        return answer