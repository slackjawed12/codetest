# 신입 사원
import sys


class Solution:
    def __init__(self, ranks):
        self.ranks = ranks

    def solve(self):
        doc_asc = sorted(self.ranks)
        result = 1
        top_index = 0
        for i in range(1, len(doc_asc)):
            cur_interview_rank = doc_asc[i][1]
            top_interview_rank = doc_asc[top_index][1]
            if cur_interview_rank < top_interview_rank:
                top_index = i
                result += 1
               
        return result


def main():
    testcase = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(testcase):
        n = int(sys.stdin.readline().strip())
        ranks = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
        sol = Solution(ranks)
        answers.append(sol.solve())

    for a in answers:
        print(a)


main()
