class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new = sorted(enumerate(score), key=lambda t:t[1], reverse=True)
        answer = ['']*len(score)
        for rank, index in enumerate(new):
            if rank == 0:
                answer[index[0]] = "Gold Medal"
            elif rank == 1:
                answer[index[0]] = "Silver Medal"
            elif rank == 2:
                answer[index[0]] = "Bronze Medal"
            else:
                answer[index[0]] = str(rank+1)
                
        return answer