with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = [list(l) for l in lines]

ox = [[int(x) for x in z] for z in a]
co = [[int(x) for x in z] for z in a]

for i in range(len(a[0])):
    v=0
    for x in ox:
        v+=1 if x[i]==1 else -1

    if v >= 0:
        if len(ox)>1:
            ox = [x for x in ox if x[i]==1]
    else:
        if len(ox)>1:
            ox = [x for x in ox if x[i]==0]

for i in range(len(a[0])):
    v=0
    for x in co:
        v+=1 if x[i]==1 else -1

    if v >= 0:
        if len(co)>1:
            co = [x for x in co if x[i]==0]
    else:
        if len(co)>1:
            co = [x for x in co if x[i]==1]

assert len(ox)==1
assert len(co)==1

print(ox[0])
print(co[0])

oxr=0
for i, v in enumerate(reversed(ox[0])):
    oxr+=2**i * v

cor=0
for i, v in enumerate(reversed(co[0])):
    cor+=2**i * v

print(oxr, cor, oxr*cor)

