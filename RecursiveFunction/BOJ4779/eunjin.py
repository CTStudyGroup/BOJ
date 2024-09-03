# 입력 받기
array = []

while True:
    try:
        line = input()
        array.append(line)
    except EOFError:
        break


def recursion(N):
    # base case
    if(N == 1):
        print("-", end="")
        return

    recursion(N//3)
    print(" "*(N//3), end="")
    recursion(N//3)


for elem in array:
    N = int(elem)
    recursion(3**N)
    print()
