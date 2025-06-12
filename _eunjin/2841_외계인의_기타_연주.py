import sys
input = sys.stdin.readline

N, P = map(int, input().split())

# 현재 누르고 있는 것보다 더 큰 수 누르려면 손 떼지 않음
# 현재 누르고 있는 것보다 더 작은 수 누르려면 손 떼야 함

curr = [[] for _ in range(N + 1)]  # 각 줄 별 누르고 있는 프렛 stack
answer = 0
for i in range(N):

    line, pret = map(int, input().split())
    if not curr[line]:  # 해당 줄에 아무것도 안누른 경우
        curr[line].append(pret)
        answer += 1

    elif curr[line][-1] > pret:  # 현재 누르고 있는 것보다 더 작은 수 내야 하는 경우
        # 손뗴기
        while curr[line] and curr[line][-1] > pret:  # curr의 마지막 수가 pret보다 작거나 같아질 때까지 pop
            curr[line].pop()
            answer += 1

        # pret 누르기
        if curr[line]:
            if curr[line][-1] < pret:
                curr[line].append(pret)
                answer += 1
        else:
            curr[line].append(pret)
            answer += 1

    elif curr[line][-1] < pret:  # 현재 누르고 있는 것보다 더 큰 수 내야 하는 경우
        curr[line].append(pret)
        answer += 1

print(answer)
