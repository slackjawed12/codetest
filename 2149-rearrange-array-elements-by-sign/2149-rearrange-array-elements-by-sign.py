class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        pos, neg = deque([n for n in nums if n > 0]), deque([n for n in nums if n < 0])
        while pos and neg:
            res.append(pos.popleft())
            res.append(neg.popleft())

        return res