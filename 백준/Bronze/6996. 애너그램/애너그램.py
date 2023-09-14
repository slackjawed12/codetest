import sys

T = int(input())

words = []
for _ in range(T):
    words.append(sys.stdin.readline().strip())

result = []
for word in words:
    pair = word.split()
    A, B = ["".join(sorted(list(w))) for w in pair]
    if A == B:
        result.append(pair[0] + " & " + pair[1] + " are anagrams.")
    else:
        result.append(pair[0] + " & " + pair[1] + " are NOT anagrams.")

print("\n".join(result))