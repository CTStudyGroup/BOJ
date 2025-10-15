# 3 - 1 == 2 ??
# 백트래킹으로 탐색

import sys
input = sys.stdin.readline

N = int(input())

found = False

def backtrack(word1: list, word2: list, concat_word: list, checking_index, minimum_index):
    global found
    if (len(word1) == checking_index):
        # print(f'{word2, concat_word}')
        if (word2 == concat_word):
            found = True
        return

    alphabet = word1[checking_index]
    tmp = concat_word[:]

    # print(f'{alphabet} 탐색중')
    count = concat_word.count(alphabet)
    
    if(count == 0):
        return
    
    same = []
    for i in range(minimum_index, len(concat_word)):
        if(alphabet == concat_word[i]):
            same.append(i)  # 통합 단어에서 해당 알파벳의 인덱스를 저장
        
    for index in same:
        element = tmp.pop(index)
        backtrack(word1, word2, tmp, checking_index + 1, index)
        if(found):
            return
        tmp.insert(index, element)

for i in range(N):
    word1, word2, concat_word = input().split()
    
    found = False
    backtrack(list(word1), list(word2), list(concat_word), 0, 0)

    if(found):
        print(f'Data set {i+1}: yes')
    else:
        print(f'Data set {i+1}: no')

