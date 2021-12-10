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
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score = 0

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
                score += scores[c]
                break

print(score)
