from collections import deque

N = int(input())
queuestack = list(map(int, input().split()))
elements = list(map(int, input().split()))
M = int(input())
insert_list = list(map(int, input().split()))

zipper = list(zip(queuestack, elements))
queue = deque([element[1] for element in filter(lambda x: x[0] == 0, zipper)])

answer = []
for x in insert_list:
    if queue:
        result = queue.pop()
        queue.appendleft(x)
        answer.append(result)
    else:
        # 큐가 아예 없으면 들어온 값 그대로 출력
        answer.append(x)

print(*answer)