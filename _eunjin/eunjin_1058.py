N = int(input())

matrix = [list(input()) for _ in range(N)]

_dict = {}

for y in range(N):
    for x in range(N):
        if matrix[y][x] == "Y":
            if y in _dict:
                _dict[y].append(x)
            else:
                _dict[y] = [x]

# print(_dict)

max_value = 0

for key in _dict.keys():
    arr = [] + _dict[key]

    for n in _dict[key]:
        arr += _dict[n]

    _set = set(arr)
    _set.discard(key)

    # print(_set)

    max_value = max(max_value, len(_set))

print(max_value)
