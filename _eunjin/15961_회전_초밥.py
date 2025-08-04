import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
C -= 1  # 0-base

dishes = []
for _ in range(N):
    dishes.append(int(input()) - 1)

# 슬라이딩 윈도우로 되나??
# 전체 N개를 k만큼의 구간을 가지고 구간을 한칸씩 이동해가면서 초밥 가짓수 구하기

started = False
eat = [0] * D  # d번 초밥을 먹은 횟수
cnt = 0  # 먹은 초밥 가짓수

start = 0
end = K - 1

for i in range(start, end + 1):
    if eat[dishes[i]] == 0:
        cnt += 1
    eat[dishes[i]] += 1

answer = cnt

if not eat[C]:  # 쿠폰 사용
    answer += 1

while True:
    if start == 0 and started:  # 한바퀴 다 돌았으므로 종료
        break

    if start == 0:  # 출발 시점은 이미 계산 다 했으므로
        started = True
    else:
        # start 부분
        eat[dishes[start - 1]] -= 1
        if eat[dishes[start - 1]] == 0:
            cnt -= 1

        # end 부분
        if eat[dishes[end]] == 0:
            cnt += 1
        eat[dishes[end]] += 1

        if not eat[C]:  # 쿠폰 사용
            answer = max(answer, cnt + 1)
        else:
            answer = max(answer, cnt)

    start = (start + 1) % N
    end = (end + 1) % N

print(answer)
