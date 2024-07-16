class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        while mainTank:
                if mainTank >= 5:
                    mainTank -= 5
                    if additionalTank > 0:
                        mainTank += 1
                        additionalTank -= 1
                    result += 5*10
                else:
                    sub = mainTank
                    mainTank = 0
                    result += sub * 10
        
        return result