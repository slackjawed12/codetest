class Solution:
    months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    def reformatDate(self, date: str) -> str:
        month_dict={mon:self.padzero_int(i+1) for i, mon in enumerate(self.months)}
        d, m, y = date.split()
        day = self.padzero(d[:-2])
        month = month_dict[m]
        return y+"-"+month+"-"+day

    def padzero_int(self, t:int) -> str:
        return "0"+str(t) if t <= 9 else str(t)

    def padzero(self, t:str) -> str:
        return "0"+t if int(t) <= 9 else t