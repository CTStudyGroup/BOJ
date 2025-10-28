import sys

input = sys.stdin.readline
# m은 행, n은 열
M, N = map(int, input().split())

# 색종이 장 수
K = int(input())

# 잘못 칠해진 칸의 개수
t = int(input())
mistaken = []
x_line = [0]*N
y_max = 0
for _ in range(t) :
    y, x = map(int, input().split())
    y, x = y-1, x-1
    mistaken.append([y, x])
    y_max = max(y_max, y)
    x_line[x] = 1
y_max += 1



def possible(paper_len) :
    
    paper_cnt = 0
    idx = 0
    
    while idx < N :
        if x_line[idx] == 1 :
            paper_cnt += 1
            idx += paper_len
        else :
            idx += 1
    return paper_cnt

# 이진 탐색 시작
l, r = y_max, max(M, N)
while l < r :
    mid = (l + r) // 2
    if possible(mid) <= K :
        r = mid
    else :
        l = mid + 1
print(r)
    
