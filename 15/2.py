import numpy as np

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = np.array([[int(x) for x in l] for l in lines])

l = len(a)

div = np.full((l,l), 9)

af = np.tile(a, (5,5))
col = 1
row = 0
for x in range(24):

    if col == 0:
        af[col * l: col * l + l, row * l:row * l + l] = \
            np.mod(af[col * l: col * l + l, row * l - l:row * l] , div) + 1
    else:
        af[col * l: col * l + l, row * l:row * l + l] = \
            np.mod(af[col * l - l: col * l, row * l:row * l + l] , div) + 1
    col+=1
    if col==5:
        col = 0
        row += 1

#print(af[0:l, l:2*l])
#exit()

def walk(a):
    b = {}
    unvisited = {}
    marked = {}
    for x in range(len(a)):
        for y in range(len(a)):
            b[(x,y)] = 100500
            unvisited[(x,y)] = 100500
    b[(0,0)] = 0
    unvisited[(0,0)] = 0
    marked[(0,0)] = 0

    while len(unvisited) > 0:
        if len(marked) > 0:
            p = (0,0)
            ml = 100500
            for np, l in marked.items():
                if l < ml:
                    p = np
                    ml = l
        else:
            p, _ = unvisited.popitem()

        x = p[0]
        y = p[1]
        ns = [c for c in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)] \
            if c[0]>=0 and c[0] < len(a[0]) and c[1] >=0 and c[1] < len(a) \
                and c in unvisited.keys()]

        del(unvisited[p])
        del(marked[p])
        for n in ns:
            cr = b[p] if p != (0,0) else 0
            if cr + a.item(n) < b[n]:
                b[n] = cr + a.item(n)
                unvisited[n] = cr + a.item(n)
                marked[n] = cr + a.item(n)


    return b[(len(a)-1, len(a)-1)]

print(walk(af))
