import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

# dp 아님
# 그냥 풀어야 된다

L.sort()

start = 0
end = N - 1
answer = 0
while start != end:
    if L[start] > 0:  # 끊을 수 있는 고리 남은 경우
        L[start] -= 1  # 고리 끊고
        end -= 1  # 제일 긴 체인과 연결
        answer += 1
    else:  # 끊을 수 있는 고리 없으면 다음 체인으로 넘어가기
        start += 1

print(answer)
