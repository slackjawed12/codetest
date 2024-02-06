import sys

T = int(sys.stdin.readline().strip())
answers = []
for _ in range(T):
    points = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(4)]
    points.sort(key=lambda x: (x[0], x[1]))
    vectors = [(points[0][0] - points[1][0], points[0][1] - points[1][1]),
               (points[0][0] - points[2][0], points[0][1] - points[2][1]),
               (points[1][0] - points[3][0], points[1][1] - points[3][1]),
               (points[2][0] - points[3][0], points[2][1] - points[3][1])]

    lengths = set([vec[0] ** 2 + vec[1] ** 2 for vec in vectors])
    inner = vectors[0][0] * vectors[1][0] + vectors[0][1] * vectors[1][1]
    if inner == 0 and len(lengths) == 1:
        answers.append(1)
    else:
        answers.append(0)

for a in answers:
    print(a)
