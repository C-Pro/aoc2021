import re

with open("input.txt", "rt") as fi:
    s=fi.read().strip()

# everybody loves regexp
m = re.match("[^\d\-]+([\-0-9]+)\.\.([\-0-9]+)[^\d\-]+([\-0-9]+)\.\.([\-0-9]+)", s)
x1, x2, y1, y2 = [int(x) for x in m.groups()]

def comp(x, y, target):
    xs = target[:2]
    ys = target[2:]

    if x <= max(xs) and x >= min(xs):
        if y <= max(ys) and y >= min(ys):
            return 0

    if x < max(xs) and y > min(ys):
        return None

    # overshoot
    if x > max(xs) or y < min(ys):
        return 1

    # need moar pwr
    return -1

def pewpew(dx, dy, target):
    x, y = 0, 0
    maxy = 0
    while comp(x, y, target) is None:
        x += dx
        y += dy
        if y > maxy:
            maxy = y
        if dx > 0:
            dx -= 1
        dy -= 1

    return (comp(x, y, target), maxy)

target = (x1, x2, y1, y2)


cnt = 0

for dx in range(1, max(x1,x2)+1):
    for dy in range(-(max(x1,x2)+1), (max(x1,x2)+1)):
        r, my = pewpew(dx, dy, target)
        if r == 0:
            cnt += 1

print(cnt)
