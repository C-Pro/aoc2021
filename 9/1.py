m = {}
row = 0
col = 0
with open("input.txt", "rt") as fi:
    for l in fi.read().splitlines():
        for v in [int(c) for c in l]:
            m[(row,col)] = v
            col +=1
        col = 0
        row += 1

def is_low(k):
    global m

    neighbours = [x for x in [m.get((k[0] + mask[0],k[1] + mask[1])) for mask in [(-1, 0), (1, 0), (0, -1), (0, 1)]] if x is not None]
    #print(k, neighbours)
    return m[k] < min(neighbours)

s = 0
for k in m:
    if is_low(k):
        #print("LOW", k)
        s+=m[k]+1

print(s)
