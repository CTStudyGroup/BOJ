import heapq

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

# heap 생성
cards = []

for card in card_list:
    heapq.heappush(cards, card)

for _ in range(M):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    heapq.heappush(cards, card1+card2)
    heapq.heappush(cards, card1+card2)


print(sum(cards))
