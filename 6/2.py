fish = {i:0 for i in range(9)}

with open("input.txt", "rt") as fi:
    a=[int(s) for s in fi.read().split(',')]



def add(v, x):
        v[x] +=1

for x in a:
    add(fish, x)


for day in range(256):
    _fish = {8: fish[0]}

    for i in range(1,9):
        _fish[i-1]=fish[i]

    _fish[6]+=fish[0]
    fish = _fish

print(sum([v for v in fish.values()]))
