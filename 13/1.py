import re
import numpy as np
from collections import deque

dots = []
folds = []
state = 0
mx, my = 0, 0
with open("input.txt", "rt") as fi:
    for l in fi.read().splitlines():
        if len(l) == 0:
            state = 1
            continue

        if state == 0:
            x, y = [int(x) for x in l.split(",")]
            dots.append((x,y))
            if x > mx:
                mx = x
            if y > my:
                my = y
        else:
            m = re.match(r"fold along ([a-z]+)=([0-9]+)", l)
            folds.append((m[1], int(m[2])))


t = np.zeros(shape=(my+1, mx+1))
for d in dots:
    t[d[1], d[0]] = 1

for f in folds:
    if f[0] == "y":
        a, b, c = 0, f[1], t.shape[0]
        if b - a > c - b:
            o = b-(c-b)
            t[o:b] = t[o:b] + np.flip(t[b:], axis=0)
            t = t[a:b]
        else:
            tt = np.flip(t[b+1:], axis=0)
            t = tt[tt.shape[0]-b:] + t[:b]

    if f[0] == "x":
        a, b, c = 0, f[1], t.shape[1]
        if b - a > c - b:
            o = b-(c-b)
            t[:, o:b] = t[:, o:b] + np.flip(t[:,b:], axis=1)
            t = t[a:b]
        else:
            tt = np.flip(t[:, b+1:], axis=1)
            t = tt[:, tt.shape[1]-b:] + t[:,:b]
    break


print(np.count_nonzero(t))
