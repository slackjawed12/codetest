class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        cur = 1
        for num in target:
            while cur != num:
                result.append('Push')
                result.append('Pop')
                cur += 1

            result.append('Push')
            cur += 1
        
        return result