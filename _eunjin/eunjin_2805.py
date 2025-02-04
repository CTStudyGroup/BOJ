N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = 1e9

max_height = 0


def cut(h):
    global trees
    ret = 0

    for tree in trees:
        if tree > h:
            ret += tree-h
    return ret


while start <= end:
    mid = (start+end)//2
    cut_result = cut(mid)

    if cut_result >= M:
        max_height = mid
        start = mid+1
    else:
        end = mid-1

print(int(max_height))
