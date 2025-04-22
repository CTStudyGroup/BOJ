import sys
input = sys.stdin.readline

d = [[0, 1, 2],  # 가로
     [3, 4, 5],
     [6, 7, 8],
     [0, 3, 6],  # 세로
     [1, 4, 7],
     [2, 5, 8],
     [0, 4, 8],  # 대각선
     [2, 4, 6]]

def win(string):
    flag = []
    for k in range(8):
        x = string[d[k][0]]
        flag.append(x)
        for i in range(3):
            if x != string[d[k][i]]:
                flag[k] = 0
                break

    ret = set()
    for f in flag:
        if f == "X" or f == "O":
            ret.add(f)
    return ret

def count_valid(string):
    cnt1, cnt2, cnt3 = 0, 0, 0  # X, O, .
    for st in string:
        if st == "X":
            cnt1 += 1
        elif st == "O":
            cnt2 += 1
        else:
            cnt3 += 1

    return cnt1, cnt2, cnt3  # X, O, .


while True:
    string = input().strip()
    if string == "end":
        break
    xcnt, ocnt, dcnt = count_valid(string)
    if xcnt - ocnt < 0 or xcnt - ocnt > 1:  # 개수 조건
        print("invalid")
        continue

    wins = list(win(string))

    if dcnt > 0:  # .이 있는 경우
        if len(wins) == 2 or len(wins) == 0:  # X,O 둘 다 이기거나 비길 수 없다.
            print("invalid")
            continue
        if wins[0] == "X":  # X가 이긴 경우: X의 개수 - O의 개수 =1
            if xcnt - ocnt != 1:
                print("invalid")
                continue
        else:  # O가 이긴 경우: X의 개수 = O의 개수
            if xcnt != ocnt:
                print("invalid")
                continue
    else:  # .이 없는 경우
        if len(wins) == 2:  # X,O 둘 다 이길 수 없다.
            print("invalid")
            continue
        if len(wins) == 1 and wins[0] == "O":
            print("invalid")
            continue

    print("valid")
