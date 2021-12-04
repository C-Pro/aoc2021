with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = [list(l) for l in lines]


acc = [0]*len(a[0])

for l in a:
    for i, v in enumerate(l):
        acc[i]+=int(v)

gamma=0
epsilon=0
for i, v in enumerate(reversed(acc)):
    most=v > len(a)/2
    if most:
        gamma += 2**i
    else:
        epsilon += 2**i

print(gamma*epsilon)
