with open("input.txt", "rt") as fi:
    a=[int(s) for s in fi.read().split(',')]

print(a)
for day in range(80):
    print("day", day)
    l = len(a)
    for i in range(l):
        if a[i]==0:
            a.append(8)
            a[i]=6
        else:
            a[i]-=1

print(len(a))
