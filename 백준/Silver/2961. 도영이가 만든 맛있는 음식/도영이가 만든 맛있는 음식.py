import copy
import functools
import sys


class Permutator:
    def __init__(self, source):
        self.result = []
        self.source = source

    def set_all_combinations(self):
        for i in range(1, len(self.source) + 1):
            self.combine(i, -1, [])

    def combine(self, num, cur_index, cur_combi):
        if len(cur_combi) == num:
            self.result.append(copy.deepcopy(cur_combi))
            return

        for idx in range(cur_index + 1, len(self.source)):
            cur_combi.append(self.source[idx])
            self.combine(num, idx, cur_combi)
            cur_combi.pop()


def get_bitter_sour(combi):
    bitter, sour = 0, 1
    for c in combi:
        bitter += c[1]
        sour *= c[0]
    return {'bitter': bitter, 'sour': sour}


N = int(sys.stdin.readline().strip())
materials = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
permutator = Permutator(materials)
permutator.set_all_combinations()
infos = [get_bitter_sour(x) for x in permutator.result]
minimum = min(infos, key=lambda x: abs(x['bitter'] - x['sour']))
print(abs(minimum['bitter']-minimum['sour']))
