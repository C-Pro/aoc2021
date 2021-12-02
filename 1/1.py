with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = [int(l) for l in lines]

prev = a[0]
cnt = 0
for v in a[1:]:
    if v > prev:
        cnt+=1
    prev = v
print(cnt)
