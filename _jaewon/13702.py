# K명에게 분배할 수 있는 막걸리의 최대 용량
# N은 100,000이하. K는 1,000,000이하.
# N^2은 불가능.
# 주전자의 개수가 사람 수보다 많을 수는 없음.

N, K = map(int, input().split())
alcohol = []
for _ in range(N):
    alcohol.append(int(input()))

start = 1
end = max(alcohol)

answer = 0
while start<=end:
    mid = (start + end) // 2

    tmp = 0
    for l in alcohol:
        tmp += l // mid

    if(tmp >= K):
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)
