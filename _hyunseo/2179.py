import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
arr =[]
for _ in range(N) :
    arr.append(input().strip())
dic = defaultdict(list) 
for idx, word in enumerate(arr) :
    dic[word[0]].append((word, idx))

def check_words(w1, w2 ) :
    min_len = min(len(w1), len(w2) )
    cnt = 0
    for idx in range(min_len) :
        if w1[idx] != w2[idx] :
            return cnt
        cnt += 1
    return cnt
'''
~~^^^
TypeError: *list[1] is not a generic class -> for w2 in list[A] (배열이 아니라 수 넣음)
'''
def check_list(lst : list) :
    overlap = [0,'','']
    
    for idx, w1 in enumerate(lst[:-1]) :
        for w2 in lst[idx+1:] :
            print(w1, w2, "--")
            tmp = check_words(w1[0], w2[0])
            if tmp > overlap[0] :
                overlap = [tmp, w1[0], w2[0]]
    return overlap

answer = [0,'','']
for key in dic.keys() :
    if len(dic[key]) == 1 :
        continue
    print(dic[key])
    cnt, w1, w2 = check_list((dic[key]))
    if cnt > answer[0] :
        answer = [cnt, w1, w2]
for t in answer[1:] :
    print(t)
