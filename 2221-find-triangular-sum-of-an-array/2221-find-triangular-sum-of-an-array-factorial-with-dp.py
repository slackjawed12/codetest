class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        fact = [1 for i in range(n)]
        for i in range(1,n):
            fact[i] = fact[i-1] * i

        res = 0
        for i in range(0,n):
            res += nums[i]*fact[n-1]//fact[i]//fact[n-1-i]%10
        return res%10
