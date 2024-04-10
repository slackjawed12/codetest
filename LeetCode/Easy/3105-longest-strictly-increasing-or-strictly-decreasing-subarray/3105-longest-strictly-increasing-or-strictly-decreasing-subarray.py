class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc = []
        dec = []
        for i in range(len(nums)):
            if i == 0:
                inc.append(nums[:1])
                dec.append(nums[:1])
            else:
                if nums[i] > nums[i-1]:
                    inc.append(inc[i-1]+[nums[i]])
                    dec.append([nums[i]])
                elif nums[i] < nums[i-1]:
                    dec.append(dec[i-1]+[nums[i]])
                    inc.append([nums[i]])
                else:
                    inc.append([nums[i]])
                    dec.append([nums[i]])
                    
        inc_max = max(list(map(len, inc)))
        dec_max = max(list(map(len, dec)))
        return max(inc_max, dec_max)

