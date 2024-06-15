import bisect
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:

        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        answer = []
        for query in queries:
            index = bisect.bisect_right(nums, query)
            answer.append(index)
        return answer
    

import heapq
class Solution2:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        result = []
        for q in queries:
            cur = 0
            count = 0
            l = []
            heapq.heapify(l)
            for num in nums:
                cur += num
                heapq.heappush(l, -num)
                count += 1
                if cur > q:
                    curmax = -heapq.heappop(l)
                    count -= 1
                    cur -= curmax
            
            result.append(count)

        return result