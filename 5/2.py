import re

a=[]
minx=None
maxx=None
miny=None
maxy=None

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    for l in lines:
        m =re.match("([0-9]+),([0-9]+)\s*->\s*([0-9]+),([0-9]+)", l)
        x1, y1, x2, y2 = int(m[1]), int(m[2]), int(m[3]), int(m[4])
        a.append([x1, y1, x2, y2])
        if minx==None:
            minx = min(x1, x2)
        else:
            minx = min(minx, x1, x2)
        if maxx==None:
            maxx = max(x1, x2)
        else:
            maxx = max(maxx, x1, x2)
        if miny==None:
            miny = min(y1, y2)
        else:
            miny = min(miny, y1, y2)
        if maxy==None:
            maxy = max(y1, y2)
        else:
            maxy = max(maxy, y1, y2)


board = [[0 for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]

for l in a:
    x1, y1, x2, y2 = l
    if x1 == x2:
        x = x1
        for y in range(min(y1, y2), max(y1, y2)+1):
            board[y-miny][x-minx] += 1
    elif y1 == y2:
        y = y1
        for x in range(min(x1, x2), max(x1, x2)+1):
            board[y-miny][x-minx] += 1
    else:
        if x1<x2:
            y=y1
        else:
            y=y2
        if y == min(y1, y2):
            yi=1
        else:
            yi=-1
        for x in range(min(x1, x2), max(x1, x2)+1):
            board[y-miny][x-minx] += 1
            y+=yi


cnt = 0
for y in range(len(board)):
    for x in range(len(board[0])):
        #print(board[y][x], end="")
        if board[y][x]>1:
            cnt+=1
    #print()

print(cnt)
