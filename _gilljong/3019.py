from sys import stdin as s

s = open("txt/3019.txt", "r")

C, P = map(int, s.readline().split())

board = list(map(int,s.readline().split()))

block = [[0,0],[-1,0]]

def count_blocks(pattern):
    cnt = 0
    for l, c in pattern:
        for i in range(C - l + 1):
            if c(i):
                cnt += 1
    return cnt

def block1(): # 1번 블록
    return count_blocks([
        (1, lambda i: board[i] >= 0),
        (4, lambda i: board[i] == board[i+1] == board[i+2] == board[i+3])
    ])

def block2(): # 2번 블록
    return count_blocks([
        (2, lambda i: board[i] == board[i+1])
    ])

def block3(): # 3번 블록
    return count_blocks([
        (3, lambda i: board[i] == board[i+1] == board[i+2] - 1),
        (2, lambda i: board[i] - 1 == board[i+1])
    ])

def block4(): # 4번 블록
    return count_blocks([
        (3, lambda i: board[i] - 1 == board[i+1] == board[i+2]),
        (2, lambda i: board[i] == board[i+1] - 1)
    ])

def block5(): # 5번 블록
    return count_blocks([
        (3, lambda i: board[i] == board[i+1] == board[i+2]),
        (3, lambda i: board[i] - 1 == board[i+1] == board[i+2] - 1),
        (2, lambda i: board[i] - 1 == board[i+1]),
        (2, lambda i: board[i] == board[i+1] - 1)
    ])

def block6(): # 6번 블록
    return count_blocks([
        (3, lambda i: board[i] == board[i+1] == board[i+2]),
        (2, lambda i: board[i] - 2 == board[i+1]),
        (3, lambda i: board[i] == board[i+1] - 1 == board[i+2] - 1),
        (2, lambda i: board[i] == board[i+1])
    ])

def block7(): # 7번 블록
    return count_blocks([
        (3, lambda i: board[i] == board[i+1] == board[i+2]),
        (2, lambda i: board[i] == board[i+1]),
        (3, lambda i: board[i] - 1 == board[i+1] - 1 == board[i+2]),
        (2, lambda i: board[i] == board[i+1] - 2)
    ])

blocks = {1: block1(), 2: block2(), 3: block3(), 4: block4(), 5: block5(), 6: block6(), 7: block7()}
print(blocks[P])

# 20m 27s