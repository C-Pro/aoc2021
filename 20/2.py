import numpy as np
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    m = [1 if c == '#' else 0 for c in lines[0]]
    a = np.array([[1 if c == '#' else 0 for c in l] for l in lines[2:]])

def pp(a):
    s = a.shape
    for r in range(s[1]):
        for c in range(s[0]):
            if a.item((r,c)) > 0:
                print("#", end="")
            else:
                print(".", end="")
        print()

def mask2int(a, c, r):
    mask = [(-1,-1), (0,-1), (1,-1), (-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)]
    res = 0
    i = 8
    for v in [a[r+off[1], c+off[0]] for off in mask]:
        res += 2**i * v
        i -= 1
    return int(res)

pad = 3
for s in range(0,50):
    a = np.pad(a, pad, constant_values=s%2)
    #pp(a)
    if s%2==0:
        b = np.zeros(shape=a.shape)
    else:
        b = np.ones(shape=a.shape)
    cols = b.shape[0]
    rows = b.shape[1]

    for c in range(1, cols-1):
        for r in range(1, rows-1):
            mi = mask2int(a, c, r)
            #print(c, r, mi)
            b[r,c] = m[mi]

    a = b[1:cols-1, 1:rows-1]
    #pp(a)


print(np.count_nonzero(a))
