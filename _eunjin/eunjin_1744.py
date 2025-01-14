N = int(input())

pos = []
neg = []
zero = False

for _ in range(N):
    n = int(input())
    if n > 0:
        pos.append(n)
    elif n < 0:
        neg.append(n)
    else:
        zero = True

pos.sort(reverse=True)
neg.sort()

# 양수, 음수 나누어서 저장 후 정렬
# 양수는 큰 순서대로 묶고 나머지는 더하기
# 양수 중에서 1은 묶지 않고 더하기
# 음수는 작은 순서대로 묶고 나머지 더하기
# 0이 있고 음수가 짝수개인 경우 모든 음수를 묶고 0을 그냥 더하기
# 0이 있고 음수가 홀수개인 경우 가장 큰 음수 * 0해서 더하기, 나머지는 서로 묶기
# 0의 개수는 상관x 어차피 음수 중에서 짝이 안지어지고 남아있는 애 하나만을 무효화시키면 됨

# 양수 묶기
pos_total = 0
pos_target = pos
if 1 in pos:
    i = pos.index(1)
    pos_target = pos[:i]
    pos_total += len(pos)-i

for i in range(0, len(pos_target), 2):
    if i+1 < len(pos_target):
        pos_total += pos_target[i]*pos_target[i+1]
    else:
        pos_total += pos_target[i]

# print(pos_total)

# 음수 묶기
neg_total = 0
for i in range(0, len(neg), 2):
    if i+1 < len(neg):
        neg_total += neg[i]*neg[i+1]
    else:
        if not zero:
            neg_total += neg[i]

# print(neg_total)

print(pos_total+neg_total)
