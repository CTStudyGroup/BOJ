from collections import deque

N = int(input())
sentences = [deque(input().split()) for _ in range(N)]
L = deque(input().split())

# print(sentences)
# print(L)

while L:
    flag = False
    for sentence in sentences:
        if sentence:
            # print("L[0]:", L[0], ", sentence[0]:", sentence[0])
            if sentence[0] == L[0]:
                sentence.popleft()
                L.popleft()
                flag = True
                break

    if not flag:
        print("Impossible")
        exit()

for sentence in sentences:
    if sentence:
        print("Impossible")
        exit()

print("Possible")
