# 입력 받기
N = int(input())

arr = []
for i in range(N):
    arr.append(i+1)

result = []


def perm(level):
    if(level == N):
        for elem in result:
            print(elem, end=" ")
        print()
        return

    for i in range(N):
        if(arr[i] in result):
            continue

        result.append(arr[i])

        perm(level+1)
        result.remove(arr[i])


perm(0)


# # 다른 풀이
# from itertools import permutations


# N = int(input())

# for permutation in permutations(range(1, N + 1),N):
# 	for elem in permutation:
# 		print(elem,end=" ")
# 	print()
