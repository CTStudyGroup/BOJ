import sys
input = sys.stdin.readline

N = int(input())
honey = list(map(int, input().split()))

# 벌통이 가장 왼쪽/가장 오른쪽/가운데에 위치하는 경우
# 벌통을 가장 왼쪽/오른쪽에 위치하는 경우 -> 벌 한마리는 벌통 반대편 제일 끝에 위치시키기
# 나머지 한마리의 위치를 O(N)으로 찾기

r_psum = [0] * N  # 왼쪽 -> 오른쪽 누적합
r_psum[0] = honey[0]
for i in range(1, N):
    r_psum[i] = r_psum[i - 1] + honey[i]

l_psum = [0] * N  # 오른쪽 -> 왼쪽 누적합
l_psum[N - 1] = honey[N - 1]
for i in range(N - 2, -1, -1):
    l_psum[i] = l_psum[i + 1] + honey[i]


# 벌통 가장 오른쪽에 두는 경우
bee1 = r_psum[N - 1] - honey[0]  # 가장 왼쪽에 벌 ~ 벌통
right = 0

for i in range(1, N - 1):
    bee2 = r_psum[N - 1] - r_psum[i]  # 두번째 벌 ~ 벌통
    curr = bee1 - honey[i] + bee2
    right = max(right, curr)


# 벌통 가장 왼쪽에 두는 경우
bee1 = l_psum[0] - honey[N - 1]  # 가장 오른쪽에 벌 ~ 벌통
left = 0

for i in range(N - 2, 0, -1):
    bee2 = l_psum[0] - l_psum[i]
    curr = bee1 - honey[i] + bee2
    left = max(left, curr)


# 벌통 가운데(가장 꿀 많은 곳)에 두는 경우
# 벌통 가운데에 위치하는 경우 -> 벌을 가장 왼쪽/오른쪽에 한마리씩 위치시키기
mid = r_psum[N - 1] - honey[0] - honey[N - 1]
mid += max(honey[1:N - 1])

print(max(right, left, mid))
