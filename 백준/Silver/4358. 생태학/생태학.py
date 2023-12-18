import sys
from collections import Counter

trees = list(map(lambda x: x.strip(), sys.stdin.readlines()))
counter = Counter(trees)
ratio = {x: counter[x] / len(trees) * 100 for x in counter}
answer = [[x, ratio[x]] for x in ratio]
answer.sort(key=lambda x: x[0])
for tree in answer:
    print("%s %.4f" % (tree[0], tree[1]))
