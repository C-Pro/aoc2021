with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = [int(l) for l in lines]

prev = sum(a[0:3])
cnt = 0
for i in range(len(a)-3):
    v = prev - a[i] + a[i+3]
    if v > prev:
        cnt+=1
    prev = v
print(cnt)
