import sys

N = int(sys.stdin.readline().strip())
info = [sys.stdin.readline().strip().split() for _ in range(N)]
dictionary = [{"name": i[0], "kor": int(i[1]), "eng": int(i[2]), "math": int(i[3])} for i in info]
dictionary.sort(key=lambda x: (-x['kor'], x['eng'], -x['math'], x['name']))
for item in dictionary:
    print(item['name'])