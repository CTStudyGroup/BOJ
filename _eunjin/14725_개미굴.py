import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    data = input().split()
    k, arr = int(data[0]), data[1:]

    curr_tree = tree  # 탐색할 부분 트리

    for food in arr:
        if food not in curr_tree:
            curr_tree[food] = {}
        curr_tree = curr_tree[food]

# {
#     'KIWI': {
#         'BANANA': {},
#         'APPLE': {}
#     },
#     'APPLE': {
#         'APPLE': {},
#         'BANANA': {
#             'KIWI': {}
#         }
#     }
# }

def dfs(_dict, depth):
    for key in sorted(_dict.keys()):
        print('--' * depth + key)
        dfs(_dict[key], depth + 1)

dfs(tree, 0)
