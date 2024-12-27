class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        same = []
        greater = []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n == pivot:
                same.append(n)
            else:
                greater.append(n)

        return less+same+greater
        