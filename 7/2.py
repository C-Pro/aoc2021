with open("input.txt", "rt") as fi:
    a=[int(s) for s in fi.read().split(',')]

mean = sum(a)//len(a)
c = [i for i in range(mean-1, mean+2)]

def pro(x):
    return ((x+1)*x)//2

m = 102938902381409318240932184
for median in c:
 s = sum([pro(abs(x-median)) for x in a])
 if m > s:
     m = s

print(m)
