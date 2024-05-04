class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        acc_sum = [0]
        for num in nums:
            acc_sum.append(acc_sum[-1] + num)
        
        acc_sum.append(acc_sum[-1])
        for i in range(1, len(acc_sum)-1):
            if acc_sum[i-1] == acc_sum[-1] - acc_sum[i]:
                return i-1

        return -1