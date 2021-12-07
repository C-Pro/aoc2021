with open("input.txt", "rt") as fi:
    a=[int(s) for s in fi.read().split(',')]

s = sorted(a)
mid = len(a) // 2
c = [s[mid]]
if len(a) % 2 == 0:
    c.append(s[mid+1])

m = 102938902381409318240932184
for median in c:
 s = sum([abs(x-median) for x in a])
 if m > s:
     m = s

print(m)
