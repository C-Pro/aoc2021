m = {}
row = 0
col = 0
with open("input.txt", "rt") as fi:
    for l in fi.read().splitlines():
        for v in [int(c) for c in l]:
            m[(row,col)] = v
            col +=1
        col = 0
        row += 1

def is_low(k):
    global m

    neighbours = [x for x in [m.get((k[0] + mask[0],k[1] + mask[1])) for mask in [(-1, 0), (1, 0), (0, -1), (0, 1)]] if x is not None]
    #print(k, neighbours)
    return m[k] < min(neighbours)

lows = []
for k in m:
    if is_low(k):
        lows.append(k)

def basinsize(k):
    global m
    been = set({})
    tovisit = set({})

    neighbours = [(k[0] + mask[0], k[1] + mask[1]) for mask in [(-1, 0), (1, 0), (0, -1), (0, 1)] if m.get((k[0] + mask[0],k[1] + mask[1])) is not None]
    tovisit.update(set([n for n in set(neighbours).difference(been) if m[n] > m[k] and m[n] < 9]))

    while len(tovisit)>0:
        newvisit = set({})
        for k in tovisit:
            neighbours = [(k[0] + mask[0], k[1] + mask[1]) for mask in [(-1, 0), (1, 0), (0, -1), (0, 1)] if m.get((k[0] + mask[0],k[1] + mask[1])) is not None]
            newvisit.update(set([n for n in set(neighbours).difference(been) if m[n] > m[k] and m[n] < 9]))
            been.add(k)
        tovisit=newvisit
    return len(been)+1

sizes=[]
for k in lows:
    bs = basinsize(k)
    print(k, bs)
    sizes.append(bs)
p = 1
for x in sorted(sizes, reverse=True)[:3]:
    p *= x
print(p)
