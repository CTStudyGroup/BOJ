# import sys
# input = sys.stdin.readline

# # 트라이
# # arr 내림차순 정렬한 뒤에 앞에서부터 트라이에 노드 추가

# class Node(object):
#     def __init__(self, key, data=None):
#         self.key = key  # 값으로 입력될 문자
#         self.data = data  # 문자열 종료 여부 flag
#         self.children = {}

# class Trie:
#     def __init__(self):
#         self.head = Node(None)

#     def insert(self, string):
#         current_node = self.head

#         for char in string:
#             if char not in current_node.children:
#                 current_node.children[char] = Node(char)
#             current_node = current_node.children[char]
#         current_node.data = string

#     def search(self, string):
#         current_node = self.head

#         for char in string:
#             if char in current_node.children:
#                 current_node = current_node.children[char]
#             else:
#                 return False

#         if current_node.data:
#             return True
#         else:
#             return False

#     def starts_with(self, prefix):
#         current_node = self.head
#         words = []

#         for p in prefix:
#             if p in current_node.children:
#                 current_node = current_node.children[p]
#             else:
#                 return None

#         current_node = [current_node]
#         next_node = []

#         while True:
#             for node in current_node:
#                 if node.data:
#                     words.append(node.data)
#                 next_node.extend(list(node.children.values()))
#             if len(next_node):
#                 current_node = next_node
#                 next_node = []
#             else:
#                 break

#         return words


# T = int(input())
# for _ in range(T):
#     N = int(input())
#     arr = []
#     trie = Trie()
#     answer = "YES"

#     for _ in range(N):
#         num = input().strip()
#         arr.append(num)

#     arr.sort(reverse=True)

#     for word in arr:
#         trie.insert(word)

#         startWith = trie.starts_with(word)

#         if len(startWith) > 1:
#             answer = "NO"
#             break

#     print(answer)

# 트라이 사용 안한 풀이
import sys
input = sys.stdin.readline

def solve(numbers):
    numbers.sort()

    for i in range(len(numbers) - 1):  # 정렬되어 있으므로 i번째는 i+1번째와만 비교해보면 된다
        if numbers[i] == numbers[i + 1][0:len(numbers[i])]:
            print("NO")
            return False

    print("YES")
    return True

t = int(input())

for _ in range(t):
    numbers = []
    n = int(input())
    for _ in range(n):
        numbers.append(input().strip())
    solve(numbers)
