from collections import deque

m = {}
with open("input.txt", "rt") as fi:
    for l in fi.read().splitlines():
        a, b = l.split("-")
        if a not in m.keys():
            m[a] = []
        if b not in m.keys():
            m[b] = []
        if a != "end" and  b != "start":
            m[a].append(b)
        if b != "end" and a != "start":
            m[b].append(a)


def walk(m, a, s):
    cnt = 0
    print(a, s)
    for n in [x for x in m[a] if x not in s]:
        if n == "end":
            cnt += 1
            print(".")
            continue
        if n not in m.keys():
            continue
        _s = s.copy()
        if n.islower():
            _s.add(n)
        cnt += walk(m, n, _s)
    return cnt

print(walk(m, "start", set([])))
