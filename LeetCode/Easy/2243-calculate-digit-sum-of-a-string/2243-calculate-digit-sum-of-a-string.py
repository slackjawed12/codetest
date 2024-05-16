class Solution:
    def digitSum(self, s: str, k: int) -> str:
        sliced = s
        while len(sliced) > k:
            tokens = []
            for i in range(0, len(sliced), k):
                tokens.append(sliced[i:i+k])
            
            sums = [sum(map(int,list(token))) for token in tokens]
            sliced = "".join(map(str, sums))

        return sliced