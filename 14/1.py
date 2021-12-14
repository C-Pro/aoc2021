
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

def step(s, rules):
    for i in range(len(s)-1):
        p = s[i:i+2]
        if p not in rules.keys():
            yield p[0]
            continue
        yield p[0]
        yield rules[p]
    yield p[1]


s = start
for _ in range(10):
    s = "".join(step(s, rules))

cnt = {}
for c in s:
    if c in cnt.keys():
        cnt[c] += 1
    else:
        cnt [c] = 1


srt = sorted(cnt.values())
print(srt[-1] - srt[0])
