import sys

T = int(sys.stdin.readline().strip())
answer = []
for _ in range(T):
    n, k, t, m = list(map(int, sys.stdin.readline().strip().split()))
    submits = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
    score_data = [{'team': x, 'score': [0 for y in range(0, k + 1)], 'submit_count': 0, 'last_submit': 0}
                  for x in range(0, n + 1)]

    for index, submit in enumerate(submits):
        team, prob_id, score = submit
        score_data[team]['score'][prob_id] = max(score, score_data[team]['score'][prob_id])
        score_data[team]['submit_count'] += 1
        score_data[team]['last_submit'] = index

    sliced = score_data[1:]
    sliced.sort(key=lambda x: (-sum(x['score']), x['submit_count'], x['last_submit']))

    for index, info in enumerate(sliced):
        if info['team'] == t:
            answer.append(index+1)


for a in answer:
    print(a)