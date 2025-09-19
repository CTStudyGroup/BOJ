import sys


def sticker_fit(i, j, sticker) :
    """스티커가 해당 i,j에 들어갈 수 있으면 True 반환"""
    for dy, dx in sticker :
        if i+dy < 0 or i+dy >= N or j + dx < 0 or j + dx >= M :
            return False
        if grid[i+dy][j+dx] == 1 :
            return False
    return True

def fill_in_sticker(i, j, sticker) :
    for dy, dx in sticker :
        grid[i+dy][j+dx] = 1

def rotate_90_clockwise(sticker, h, w) :
    return [(c, h - 1 - r) for r, c in sticker]

def put_on_one_sticker(r, c, sticker):
    h, w = r, c
    for dir in range(4):
        for i in range(N - h + 1):   # 회전 후 높이 반영
            for j in range(M - w + 1):  # 회전 후 너비 반영
                if sticker_fit(i, j, sticker):
                    fill_in_sticker(i, j, sticker)
                    return

        # 방향 바꾸기
        sticker = rotate_90_clockwise(sticker, h, w)
        h, w = w, h  # 회전하면 높이와 너비가 서로 바뀜



def count_sticker_spaces() :
    count = 0
    for i in range(N) :
        for j in range(M) :
            if grid[i][j] == 1 :
                count += 1
    return count

N, M, K = map(int, input().split())
grid = [[0]*M for _ in range(N)]

def solve() :
    for _ in range(K) :
        r, c = map(int, input().split())
        m = []
        for _ in range(r) :
            m.append(list(map(int, input().split())))
        
        # 스티커 정보를 배열로 바꾸기
        sticker = []
        for i in range(r) :
            for j in range(c) :
                if m[i][j] == 1 :
                    sticker.append([i, j])
        
        # 스티커 하나 방향 돌려가면서 채워넣기
        put_on_one_sticker(r, c, sticker)

        
    # 정답을 구하기
    print(count_sticker_spaces())
solve()
