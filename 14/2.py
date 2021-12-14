
rules = {}
state = 0
with open("input.txt", "rt") as fi:
    for l in fi.read().splitlines():
        if len(l) == 0:
            state = 1
            continue

        if state == 0:
            start = l.strip()
        else:
            m = l.split("->")
            rules[m[0].strip()] = m[1].strip()


#print(start)
#print(rules)

f = {}

for i in range(len(start)-1):
    p = start[i:i+2]
    if p in f.keys():
        f[p]+=1
    else:
        f[p] = 1


for step in range(40):
    _f = f.copy()
    for p in f.keys():
        #print(_f, p, rules[p])
        if p not in rules.keys():
            continue
        if f[p] == 0:
            continue

        _f[p] -= f[p]

        r = rules[p]
        p1 = p[0] + r
        p2 = r + p[1]

        if p1 in _f.keys():
            _f[p1] += f[p]
        else:
            _f[p1] = f[p]

        if p2 in _f.keys():
            _f[p2] += f[p]
        else:
            _f[p2] = f[p]

    f = {k:v for k,v in _f.items() if v>0}

cs = {}
for p in f:
    if p[0] in cs.keys():
        cs[p[0]]+=f[p]
    else:
        cs[p[0]] = f[p]

    if p[1] in cs.keys():
        cs[p[1]]+=f[p]
    else:
        cs[p[1]] = f[p]

srt = sorted(cs.values())
print((srt[-1] - srt[0])//2+1)
