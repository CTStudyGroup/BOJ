import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())

shoot = list(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(N)]

shoot.sort()  # 이분탐색을 위해 정렬

# 각 동물마다 x값 가장 가까운 사대를 찾아서 사정거리 안에 위치하는지 확인?
# 가장 가까운 사대 찾기 = 이분탐색 = Nlog(M)

# 주어진 target 값과 가장 가까운 사대의 x좌표 찾기
# T T F F F F
def find(target):
    start = 0
    end = M - 1
    idx = -1
    min_diff = 1e9

    while start <= end:
        mid = (start + end) // 2
        diff = shoot[mid] - target  # 현재 사대와 동물 사이 거리

        if abs(diff) < min_diff:  # 거리를 최소로 만드는 사대 인덱스 갱신
            min_diff = abs(diff)
            idx = mid

        if shoot[mid] < target:
            start = mid + 1
        elif shoot[mid] > target:
            end = mid - 1
        else:
            break

    return shoot[idx]

answer = 0
for x, y in animals:
    nearest = find(x)  # 동물과 가장 가까운 사대 위치 탐색
    dist = abs(nearest - x) + y

    if dist <= L:
        answer += 1

print(answer)
