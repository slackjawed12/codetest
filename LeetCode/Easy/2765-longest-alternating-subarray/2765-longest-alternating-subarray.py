class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        head, tail = 1, 0
        result = -1
        while head < len(nums):
            if head == tail:
                head += 1
                continue

            length = head - tail + 1
            diff = nums[head] - nums[tail]

            if ((length % 2 == 0) and diff == 1) or ((length % 2 != 0) and diff == 0):
                result = max(result, length)
                head += 1
            else:
                # not alternating
                if nums[head]-nums[head-1] == 1:
                    tail = head -1
                else:
                    tail = head

        return result
