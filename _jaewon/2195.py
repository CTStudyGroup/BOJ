import sys

S = input().strip()
P = input().strip()

# P의 원소를 하나씩 탐색하면서, S와 가장 겹치는 부분이 많은 경우까지 탐색 진행
index = 0
count = 0
while index < len(P):
    current = P[index]

    sub = [] # 후보자 인덱스
    for sub_index, compare in enumerate(S):
        if(compare == current):
            sub.append(sub_index)

    maximum = 1
    for sub_index in sub:
        if (sub_index == len(S)-1):
            break

        tmp = 1
        for i in range(index+1, len(P)):
            if(sub_index + i - index == len(S)):
                break
            if(P[i] == S[sub_index + i - index]):
                tmp += 1
                maximum = max(maximum, tmp)
            else:
                break
    index += maximum
    count += 1

print(count)