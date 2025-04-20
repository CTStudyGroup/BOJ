import sys
import heapq
input = sys.stdin.readline

T = int(input())

# 우선순위큐에 넣고
# 홀수번째 이면 N//2개 뽑고 hq[0]출력하고 뽑은거 다시 넣고? = 시간초과
# left: 중앙값보다 작은 것들
# right: 중앙값 이상인 것들
for _ in range(T):
    M = int(input())
    arr = []
    I = M // 10
    if M % 10:
        I += 1
    for i in range(I):
        inp = list(map(int, input().split()))
        for elem in inp:
            arr.append(elem)
    answer = []
    lq = []  # 최대힙
    rq = []  # 최소힙

    for i in range(M):
        num = arr[i]
        if not lq or num <= -lq[0]:
            heapq.heappush(lq, -num)
        else:
            heapq.heappush(rq, num)

        if len(lq) > len(rq) + 1:
            heapq.heappush(rq, -heapq.heappop(lq))
        elif len(rq) > len(lq):
            heapq.heappush(lq, -heapq.heappop(rq))

        if i % 2 == 0:
            answer.append(-lq[0])

    print(len(answer))
    for i in range(0, len(answer), 10):
        print(' '.join(map(str, answer[i:i + 10])))

