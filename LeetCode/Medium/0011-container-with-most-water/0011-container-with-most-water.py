class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height)-1
        answer = 0
        while i < j:
            answer = max(answer, (j - i) * min(height[i], height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        return answer