N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

cards = list(range(N))
check_for_joongbok = set()
cnt = 0

# 검사 함수
def is_ok(cards):
    for i in range(N):
        if P[cards[i]] != (i % 3):
            return False
    return True

# 초기 검사
if is_ok(cards):
    print(0)
    exit()

while True:
    cards_str = ''.join(map(str, cards))
    if cards_str in check_for_joongbok:
        print(-1)
        exit()
    check_for_joongbok.add(cards_str)

    # 셔플링
    tmp = [0] * N
    for i in range(N):
        tmp[S[i]] = cards[i]
    cards = tmp
    cnt += 1

    if is_ok(cards):
        print(cnt)
        exit()
