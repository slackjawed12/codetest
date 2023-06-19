class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sort = sorted(nums)
        answer = 0
        for i in range(0, len(sort), 2):
            answer += min(sort[i], sort[i+1])
            
        return answer