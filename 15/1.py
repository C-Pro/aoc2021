import numpy as np
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = np.array([[int(x) for x in l] for l in lines])


def walk(a):

    b = {}
    unvisited = {}
    visited = set([])
    for x in range(len(a)):
        for y in range(len(a)):
            b[(x,y)] = 100500
            unvisited[(x,y)] = 100500
    b[(0,0)] = 0
    unvisited[(0,0)] = 0

    while len(unvisited) > 0:
        p = sorted(unvisited.keys(), key=lambda p: unvisited[p])[0]
        x = p[0]
        y = p[1]
        ns = [c for c in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)] \
            if c[0]>=0 and c[0] < len(a[0]) and c[1] >=0 and c[1] < len(a) \
                and c not in visited]

        del(unvisited[p])
        for n in ns:
            cr = b[p] if p != (0,0) else 0
            if cr + a.item(n) < b[n]:
                b[n] = cr + a.item(n)
                unvisited[n] = cr + a.item(n)

        visited.add(p)

    return b[(len(a)-1, len(a)-1)]

print(walk(a))
