from typing import List
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # for prefix sum S_i,
        # S_x = S_y - S_x = S_n - S_y
        # 3 * S_y = 2 * S_n
        # 2 * S_x = S_y
        prefix = [arr[0]]
        for n in arr[1:]:
            prefix.append(prefix[-1]+n)
        
        last = prefix[-1]
        y = None
        for i, n in enumerate(prefix[:-1]):
            if 3 * n == 2 * last:
                y = i
        
        if y is None:
            return False

        x = None
        for i, n in enumerate(prefix[:y]):
            if 2 * n == prefix[y]:
                x = i
        
        return x is not None