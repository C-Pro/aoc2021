import re

with open("input.txt", "rt") as fi:
    l=fi.read().splitlines()

# everybody loves regexp
p = [0,0]
m = re.match(".*: ([\-0-9]+)", l[0])
p[0] = int(m[1])

m = re.match(".*: ([\-0-9]+)", l[1])
p[1] = int(m[1])

s = [0,0]
turn = 0
cnt = 0
i = 1
su = 0
sc = 0
while True:
    cnt+=1
    if i == 101:
        i = 1

    su += i
    sc += 1
    i += 1

    if sc == 3:
        sc = 0

        p[turn] = (p[turn]+su-1) % 10 + 1
        s[turn] += p[turn]

        if s[turn] >= 1000:
            print(min(s)*  cnt)
            exit()

        turn = 1 if turn == 0 else 0

        su = 0
