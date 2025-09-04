import sys
from collections import defaultdict
S = input()
P = input()

# S에서 나올 수 있는 모든 연속 문자열 딕셔너리에 담기
# 1000^2
_dict = defaultdict(bool)
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        _dict[S[i:j]] = True

# dp?
# dp[i]: P[i]를 만드는데 드는 최소 사용횟수
# dp[i] = min(dp[i],dp[j-1]+1), j는 문자열 쪼개는 기준점
MAX = sys.maxsize
dp = [MAX] * len(P)
dp[0] = 1

for i in range(len(P)):
    if P[:i + 1] in _dict:  # 0~i번째 전체 문자열을 한번의 copy로 가능한 경우
        dp[i] = 1
        continue

    for j in range(1, i + 1):  # 0~i 문자열을 두 부분으로 쪼개서 dp 점화식
        part = P[j:i + 1]
        if part in _dict:
            dp[i] = min(dp[i], dp[j - 1] + 1)

print(dp[-1])
