class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        isBulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9
        isHeavy = mass >= 100
        
        if isBulky and isHeavy:
            return "Both"
        if isBulky and not isHeavy:
            return "Bulky"
        if isHeavy and not isBulky:
            return "Heavy"
        
        return "Neither"
        
