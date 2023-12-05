import sys
from collections import deque

N = int(sys.stdin.readline().strip())
sample_shape = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
shapes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]


def get_counter(shape):
    result = []
    for num in shape:
        if num == 1:
            result.append(3)
        elif num == 2:
            result.append(4)
        elif num == 3:
            result.append(1)
        else:
            result.append(2)
    return result


def is_same_shape(sample, target):
    sample_q = deque(sample)
    for i in range(len(sample)):
        is_equal = True
        for j, n in enumerate(sample_q):
            if n != target[j]:
                is_equal = False
                break

        if is_equal:
            return True
        else:
            sample_q.append(sample_q.popleft())

    return False


counter_sample = get_counter(sample_shape)
total = 0
answers = []
for shape in shapes:
    if is_same_shape(sample_shape, shape):
        total += 1
        answers.append(shape)
    else:
        counter_sample.reverse()
        if is_same_shape(counter_sample, shape):
            total += 1
            answers.append(shape)
        counter_sample.reverse()

print(total)
for a in answers:
    print(*a)
