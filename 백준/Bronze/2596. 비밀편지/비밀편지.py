import sys

N = int(input())
S = sys.stdin.readline().strip()

dic = {"000000": 'A', "001111": "B", "010011": "C", "011100": "D", "100110": "E",
       "101001": "F", "110101": "G", "111010": "H"}

result = []
for i in range(N):
    target = S[i * 6:i * 6 + 6]
    if target in dic:
        result.append(dic[target])
    else:
        isInDictionary = False
        for comp in dic:
            temp = int(target, 2) ^ int(comp,2)
            if int(temp) & (int(temp) - 1) == 0:
                result.append(dic[comp])
                isInDictionary = True
                break

        if not isInDictionary:
            result = [str(i+1)]
            break

print("".join(result))
