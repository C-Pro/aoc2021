from collections import deque

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

opening = list("{([<")
closing = list("})]>")

m = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}

scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

sss = []

for l in lines:
    d = deque()
    corrupt = False
    for c in l:
        if c in opening:
            d.append(c)
            continue
        if c in closing:
            pc = d.pop()
            if m[pc] != c:
                corrupt = True
                break
    if not corrupt:
        score = 0
        for c in reversed(d):
            score = score * 5 + scores[c]
        sss.append(score)

sss.sort()
print(sss[len(sss)//2])
