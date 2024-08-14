class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ch, cm = [int(c) for c in current.split(":")]
        th, tm = [int(c) for c in correct.split(":")]

        cn = ch*60 + cm
        tn = th*60 + tm
        diff = tn - cn
        result = 0
        for div in [60, 15, 5, 1]:
            result += diff // div
            diff %= div

        return result