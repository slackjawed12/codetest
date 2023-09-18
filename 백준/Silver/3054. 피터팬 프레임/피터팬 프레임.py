word = input()

result = list(map(list, ["..#..", ".#.#.", "#." + word[0] + ".#", ".#.#.", "..#.."]))

for index, c in enumerate(list(word[1:])):
    length = 4
    if (index + 2) % 3 == 0:
        result[0] += list(".*..")
        result[1] += list("*.*.")
        result[2][len(result[2]) - 1] = "*"
        result[2] += list("." + c + ".*")
        result[3] += list("*.*.")
        result[4] += list(".*..")
    else:
        result[0] += list(".#..")
        result[1] += list("#.#.")
        result[2] += list("." + c + ".#")
        result[3] += list("#.#.")
        result[4] += list(".#..")

print("\n".join(list(map(lambda x: "".join(x), result))))
