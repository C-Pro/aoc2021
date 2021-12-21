import re
from itertools import product

with open("input.txt", "rt") as fi:
    l=fi.read().splitlines()

# everybody loves regexp
p = [0,0]
m = re.match(".*: ([\-0-9]+)", l[0])
p[0] = int(m[1])

m = re.match(".*: ([\-0-9]+)", l[1])
p[1] = int(m[1])

def key(p,s):
    return (p[0], p[1], s[0], s[1])

mem = {}
def calc(p, s):
    if key(p, s) in mem.keys():
        return mem[key(p, s)]

    scores = [0, 0]
    for su in [sum(x) for x in product([1,2,3], repeat=3)]:
        _p = (p[0] + su -1) % 10 + 1
        _s = s[0] + _p

        if _s >= 21:
            scores[0] += 1
        else:
            d = calc((p[1], _p), (s[1], _s))
            scores[0] += d[1]
            scores[1] += d[0]

    mem[key(p,s)] = scores
    return scores

s = [0,0]
print(max(calc(p, s)))
