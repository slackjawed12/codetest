import sys

N = int(sys.stdin.readline().strip())
desks = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

answer = (0, 0)
for grade in range(1, 6):
    start, end = 0, 0
    while end < N:
        start_desk = desks[start]
        end_desk = desks[end]
        if grade not in start_desk:
            start += 1
            end += 1
        elif grade in end_desk:
            end += 1
        elif grade not in end_desk:
            answer = (end - start, grade) if answer[0] < end - start else answer
            start = end

    answer = (end - start, grade) if answer[0] < end - start else answer

print(*answer)
