import re

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    nums = [int(s) for s in lines[0].split(",")]

    boardn=-1
    boards=[]
    board=[]
    for i, l in enumerate(lines[1:]):
        if l=="":
            if boardn>=0:
                boards.append(board[:])
                board=[]
            boardn+=1
            continue
        board.append([int(s) for s in re.findall("[0-9]+", l)])
    boards.append(board[:])

def check(board):
    for row in board:
        if all([x==-1 for x in row]):
            return True
    for j in range(len(board[0])):
        if all([x[j]==-1 for x in board]):
            return True
    return False

def sum_unmarked(board):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                s+=board[i][j]
    return s


def mark(board, n):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == n:
                board[i][j] = -1


ans = 0
for n in nums:
    j = []
    for i, board in enumerate(boards):
        mark(board, n)
        if check(board):
            if len(boards)==1:
                print(n * sum_unmarked(board))
            j.append(i)
    boards = [b for i,b in enumerate(boards) if i not in j]
