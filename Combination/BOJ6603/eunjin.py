
choice = []


def comb(index, level, K, line):
    # base case
    if(level == K):
        for elem in choice:
            print(elem, end=" ")
        print()

    for i in range(index, len(line)):
        choice.append(line[i])
        comb(i+1, level+1, K, line)
        choice.pop()


while True:
    line = list(map(int, input().split()))

    k, arr = line[0], line[1:]

    if k == 0:
        break

    comb(0, 0, 6, arr)
    print()
