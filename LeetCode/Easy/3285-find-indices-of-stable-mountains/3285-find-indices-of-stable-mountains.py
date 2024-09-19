from typing import List

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i, h in enumerate(height) if i > 0 and height[i-1] > threshold]