import sys

infos = []
while True:
    page = int(sys.stdin.readline().strip())
    if page == 0:
        break

    info = sys.stdin.readline().strip()
    infos.append([page, info])

for info in infos:
    page = info[0]
    pageRanges = info[1].split(',')
    pages = []
    for pageRange in pageRanges:
        startEnd = list(map(int, pageRange.split('-')))
        start, end = startEnd[0], startEnd[-1]
        target = [i for i in range(start, end + 1) if i <= page and i not in pages]
        pages += target

    print(len(pages))