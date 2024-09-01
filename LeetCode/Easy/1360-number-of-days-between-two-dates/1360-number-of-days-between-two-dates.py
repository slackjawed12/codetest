class Solution:
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        cnt1 = self.datesFromOrigin(date1)
        cnt2 = self.datesFromOrigin(date2)

        return abs(cnt1-cnt2)
    
    def isLeapYear(self, year:int)->bool:
        if year % 4 != 0:
            return False
        if year % 100 == 0 and year % 400 != 0:
            return False

        return True
    
    def datesFromOrigin(self, date:str) -> int:
        oy, om, od = 1970, 1, 1
        cy, cm, cd = [int(x) for x in date.split("-")]
        
        result = 0
        for y in range(oy, cy):
            if self.isLeapYear(y):
                result += 366
            else:
                result += 365

        for m in range(om, cm):
            result += self.days[m-1]

        if cm > 2 and self.isLeapYear(cy):
            result += 1

        result += cd - od
        return result