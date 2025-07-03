import sys
import heapq
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

# 비어있는 자리 중에서 번호 가장 작은 것에 앉음
# 컴퓨터 최소 개수, 각 컴퓨터별 사용한 사람 수

# 시작 시간 순으로 정렬해 앞에서부터 배정
info.sort(key=lambda x: [x[0], x[1]])

pq = []  # 컴퓨터 우선순위큐 (사용 종료 시간, 컴퓨터 번호, 누적 사용자 수)

num = 0
for start, end in info:
    if pq:  # 컴퓨터가 있으면
        if pq[0][0] < start:  # 앞 사용자가 다 쓰고 나간 경우
            # 비어있는 컴퓨터 모두 찾기
            empty_computers = []
            while pq and pq[0][0] < start:
                empty_computers.append(heapq.heappop(pq))

            empty_computers.sort(key=lambda x: x[1])  # 컴퓨터 번호 순으로 정렬
            # print("empty_computers:", empty_computers)

            # 컴퓨터 사용 처리
            use = empty_computers[0]
            heapq.heappush(pq, (end, use[1], use[2] + 1))

            # 나머지 비어있는 컴퓨터는 그대로 pq에 넣기
            for i in range(1, len(empty_computers)):
                heapq.heappush(pq, empty_computers[i])
        else:  # 새 컴퓨터 추가 필요한 경우
            num += 1
            heapq.heappush(pq, (end, num, 1))
    else:  # 컴퓨터 없으면 새 컴퓨터 추가
        num += 1
        heapq.heappush(pq, (end, num, 1))


pq.sort(key=lambda x: x[1])

print(len(pq))
print(' '.join(map(str, list(user for _, _, user in pq))))
