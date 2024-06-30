class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        result = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if result == 1:
                    break

                if result != -1 and j - i + 1 >= result:
                    continue

                sub = nums[i:j+1]
                or_val = 0
                for num in sub:
                    or_val |= num
                
                if or_val >= k:
                    result = len(sub)
        
        return result

# keep the last position of the bit
class Solution2:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        bit = [-1 for _ in range(32)]
        n = len(nums)
        j, cur, res = 0, 0, -1
        for i in range(n):
            cur |= nums[i]
            for b in range(32):
                if nums[i] & (1 << b): 
                    bit[b] = i
            while cur >= k and j <= i:
                if res == -1:
                    res = i - j +1
                else:
                  res = min(res, i - j + 1)
                
                for b in range(32):
                    if nums[j] & (1 << b) and bit[b] == j:
                        bit[b] = -1
                        cur ^= (1 << b)
                j += 1     

        return res

# count the number of existing bit
class Solution3:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        bit_cnt = [0 for _ in range(32)]
        n = len(nums)
        j, cur, res = 0, 0, -1
        for i in range(n):
            cur |= nums[i]
            for b in range(32):
                if nums[i] & (1 << b): bit_cnt[b] += 1
            while cur >= k and j <= i:
                if res == -1:
                    res = i - j +1
                else:
                  res = min(res, i - j + 1)

                for b in range(32):
                    if nums[j] & (1 << b): 
                        bit_cnt[b] -= 1
                        if not bit_cnt[b]: cur ^= (1 << b)
                j += 1     

        return res
