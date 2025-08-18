# 등장하는 알파벳을 모두 다른 알파벳으로
# 자기 자신을 바꾸는 건 가능
# N이 100까지이기 때문에 완전탐색해도 5050번

# 같은 문자가 있으면 항상 같은 문자로 변환되어야 함.

N = int(input())
words = []
for _ in range(N):
    words.append(input())

count = 0
visited = [0 for _ in range(N)]

def get_duplicate_indexes(word):
    # word에서 같은 글자가 있는 인덱스를 뽑음
    dup = []
    checked = [0 for _ in range(len(word))]
    for i in range(len(word)):
        if (checked[i]):
            continue
        
        tmp = []
        for j in range(i + 1, len(word)):
            if(word[i] == word[j]):
                tmp.append(j)
                checked[j] == 1

        if (tmp):
            tmp.append(i)
            tmp.sort()
            checked[i] == 1
            dup.append(tmp)
    return dup

matrix = []
for word in words:
    dup = get_duplicate_indexes(word)
    matrix.append(dup)


for i in range(len(matrix)):
    dup = matrix[i]
    for j in range(i + 1, len(matrix)):
        compare = matrix[j]

        if (compare[:] == dup[:]):
            count += 1
            flag = 1

print(count)