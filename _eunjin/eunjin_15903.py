N, M = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(M):
    cards.sort()
    score = cards[0]+cards[1]
    cards[0] = score
    cards[1] = score

print(sum(cards))
