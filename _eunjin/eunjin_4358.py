import sys
input = sys.stdin.readline

_dict = {}
total = 0
arr = []

while True:
    current = input().strip()
    if not current:
        break

    total += 1
    if current in _dict:
        _dict[current] += 1
    else:
        _dict[current] = 1
        arr.append(current)

arr.sort()
for tree in arr:
    print(tree, f"{100*_dict[tree]/total:.4f}")
