class Solution:
    def largestInteger(self, num: int) -> int:
        l = list(str(num))
        parity = ['e' if int(i) % 2 == 0 else 'o' for i in l]
        even = [int(i) for i in l if int(i) % 2 == 0]
        odd = [int(i) for i in l if int(i) % 2 != 0]
        even.sort()
        odd.sort()

        result = []
        for p in parity:
            if p =='e':
                result.append(str(even.pop()))
            else:
                result.append(str(odd.pop()))
            
        return int("".join(result))
        