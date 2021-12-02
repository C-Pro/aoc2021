with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = [l.split() for l in lines]

x = 0
d = 0
aim = 0

for s in a:
    if s[0] == "forward":
        x+=int(s[1])
        d+=aim*int(s[1])
    if s[0] == "up":
        aim-=int(s[1])
    if s[0] == "down":
        aim+=int(s[1])

print(x*d)
