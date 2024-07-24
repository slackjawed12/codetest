class Solution:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    offset = [0]
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        for d in self.days:
            self.offset.append(self.offset[-1]+d)
        
        alice_arrive_order = self.order(arriveAlice)
        alice_leave_order = self.order(leaveAlice)
        bob_arrive_order = self.order(arriveBob)
        bob_leave_order = self.order(leaveBob)

        first_arrive = min(alice_arrive_order, bob_arrive_order)
        second_arrive = max(alice_arrive_order, bob_arrive_order)
        first_leave = min(alice_leave_order, bob_leave_order)
        second_leave = max(alice_leave_order, bob_leave_order)

        if second_arrive > first_leave:
            return 0

        if first_arrive < second_arrive and first_leave > second_leave:
            return second_leave-second_arrive+1
        
        return first_leave - second_arrive + 1
    
    def order(self, date:str)->int:
        month, day = [int(n) for n in date.split("-")]
        order = self.offset[month-1]+day
        return order
    