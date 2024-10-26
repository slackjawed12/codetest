class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high =  0, len(letters)-1
        cur = letters[high]
        if cur <= target:
            return letters[0]

        while low <= high:
            mid = (low+high)//2
            temp = letters[mid]
            if temp > target:
                high = mid-1
                cur = temp
            else:
                low = mid+1
        
        return cur
        