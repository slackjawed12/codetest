class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # acc = [3, 1, 2, 6]
        # l = 2 -> acc[1] - acc[0], acc[2] - acc[0], acc[3] - acc[1]
        acc = [0]*(len(nums) + 1)
        for i, n in enumerate(nums): 
            acc[i+1] += n + acc[i]

        result = -1
        for c in range(l,r+1):
            for i in range(c, len(acc)):
                s = acc[i] - acc[max(i-c, 0)]
                if s > 0:
                    if result < 0:
                        result = s
                    else:
                        result = min(result, s)

        return result