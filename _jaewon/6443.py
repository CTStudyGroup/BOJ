from collections import defaultdict

N = int(input())

def backtrack(dictionary, current, depth, limit, word):
    tmp = word[:]

    tmp.append(current)

    if(depth == limit):
        print(''.join(tmp))
        return
    
    for alphabet in dictionary.keys():
        if (dictionary[alphabet] > 0):
            dictionary[alphabet] -= 1
            backtrack(dictionary, alphabet, depth+1, limit, tmp)
            dictionary[alphabet] += 1
    del tmp

for _ in range(N):
    alphabets = sorted(list(input()))
    dic = defaultdict(int)

    for alphabet in alphabets:
        dic[alphabet] += 1

    for key in dic.keys():
        dic[key] -= 1
        backtrack(dic, key, 1, len(alphabets), [])
        dic[key] += 1
