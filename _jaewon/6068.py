N = int(input().strip())
tasks = []
for _ in range(N):
    t, d = map(int, input().split())
    tasks.append((t, d))  # (소요시간, 마감시간)

# 마감시간 오름차순, 마감 같으면 소요시간 짧은 순
tasks.sort(key=lambda x: (x[1], x[0]))

cum = 0
best = float('inf')

for t, d in tasks:
    cum += t               # 지금 작업까지 누적 소요시간
    best = min(best, d - cum)  # 이 시점까지 맞추려면 시작 가능 최대 시각

print(best if best >= 0 else -1)
