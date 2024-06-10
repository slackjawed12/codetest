class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        result = None
        for i, num in enumerate(nums):
            if num == target:
                dist = abs(i-start)
                if result == None:
                    result = dist
                else:
                    result = min(dist, result)

        if result == None:
            return -1

        return result
                