with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a=[{"digits": l.split(" ")[:10], "out": l.split(" ")[11:]} for l in lines]

cnt = 0
for l in a:
    for d in l["out"]:
        if len(d) in [2,3,4,7]:
            cnt+=1

print(cnt)
