from collections import defaultdict, deque

N, K = list(map(int, input().split()))
lengths = [len(input()) for _ in range(N)]

goodFriends = defaultdict(int)
count = 0
queue = deque([])

for i in range(N+K):
    if i > K:
        curr_n = queue.popleft()
        goodFriends[curr_n] -= 1
        count += goodFriends[curr_n]

    if i < N:
        queue.append(lengths[i])
        goodFriends[lengths[i]] += 1
print(count)