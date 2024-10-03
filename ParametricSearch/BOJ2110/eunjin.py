# 입력 받기
N, C = map(int, input().split())
X = []
for _ in range(N):
    X.append(int(input()))


def is_possible(h):
    global N, C, X
    sorted_arr = sorted(X)
    last_idx = 0  # 가장 첫 집에 공유기 설치하는게 무조건 이득
    cnt = 1
    # 그리디 방식으로 앞에서부터 선택해가며 간격이 h이상인지 판단한다.
    for i in range(1, N):
        if(sorted_arr[i]-sorted_arr[last_idx] >= h):
            last_idx = i
            cnt += 1

    return cnt >= C

# N이 최대 200,000이므로 브루트포스 풀이 불가능
# 가장 인접한 두 공유기 사이의 거리를 k로 뒀을 때
# 아래와 같이 어느 순간 최소 k거리를 두고 공유기 설치 불가능한 지점이 생긴다.
# 1 2 3 4 ... x-1 x x+1 x+2 ...
# T T T T      T  F  F   F


# parametric search로 x를 찾는다.
cur = -1
step = max(X)+1
while(step != 0):
    #print("started, step:", step)
    while(cur+step <= max(X)+1 and is_possible(cur+step)):
        cur += step
        #print("cur:", cur)
    step //= 2

print(cur)
