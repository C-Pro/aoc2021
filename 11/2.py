from collections import deque

m = []
with open("input.txt", "rt") as fi:
    for l in fi.read().splitlines():
        row = []
        for v in [int(c) for c in l]:
            row.append(v)
        if len(row) > 0:
            m.append(row)


def flash(k, f):
    global m
    #print(k[0],k[1])

    m[k[0]][k[1]] = 0

    msks = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (-1,1), (1, -1), (1, 1)]
    flashes = set([k])

    for r,c in [(k[0] + mask[0],k[1] + mask[1]) for mask in msks]:
        if (r,c) in f:
            continue
        if r < 0 or r > 9 or c < 0 or c > 9:
            continue
        m[r][c] +=1
        if m[r][c] > 9:
            flashes.update(flash((r,c), flashes))

    return flashes


step = 1
while True:
    flashes = set([])
    for r in range(len(m)):
        for c in range(len(m[0])):
            m[r][c]+=1
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] > 9:
                flashes.update(flash((r,c), flashes))
    if len(flashes) == len(m) * len(m[0]):
        print(step)
        break
    for r,c in flashes:
        m[r][c]=0
    step +=1
