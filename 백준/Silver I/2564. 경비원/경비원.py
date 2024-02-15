import sys

NORTH, SOUTH, WEST, EAST = 1, 2, 3, 4


class Solution:

    def __init__(self):
        self.width, self.height = list(map(int, sys.stdin.readline().strip().split()))
        n = int(sys.stdin.readline().strip())
        self.stores = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
        self.man = list(map(int, sys.stdin.readline().strip().split()))

    def get_min_distance(self):
        answer = 0
        for store in self.stores:
            dist = self.get_dist(store)
            answer += dist

        return answer

    def get_dist(self, store):
        store_dir, store_offset = store
        man_dir, man_offset = self.man

        if store_dir == man_dir:
            return abs(man_offset - store_offset)

        if man_dir == NORTH:
            if store_dir == SOUTH:
                return self.height + min(man_offset + store_offset, self.width - man_offset + self.width - store_offset)
            elif store_dir == WEST:
                return store_offset + man_offset
            elif store_dir == EAST:
                return store_offset + self.width - man_offset
        elif man_dir == SOUTH:
            if store_dir == NORTH:
                return self.height + min(man_offset + store_offset, self.width - man_offset + self.width - store_offset)
            elif store_dir == WEST:
                return self.height - store_offset + man_offset
            elif store_dir == EAST:
                return self.height - store_offset + self.width - man_offset
        elif man_dir == WEST:
            if store_dir == NORTH:
                return store_offset + man_offset
            elif store_dir == SOUTH:
                return self.height - man_offset + store_offset
            elif store_dir == EAST:
                return self.width + min(man_offset + store_offset,
                                        self.height - man_offset + self.height - store_offset)
        else:
            if store_dir == NORTH:
                return self.width - store_offset + man_offset
            elif store_dir == SOUTH:
                return self.width - store_offset + self.height - man_offset
            elif store_dir == WEST:
                return self.width + min(man_offset + store_offset,
                                        self.height - man_offset + self.height - store_offset)

        return -1


solution = Solution()
print(solution.get_min_distance())
