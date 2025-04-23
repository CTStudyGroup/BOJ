from collections import Counter

def win(testcase):
    indexes = [(0,4,8), (2,4,6), # cross
         (0,1,2), (3,4,5), (6,7,8), # row
         (0,3,6), (1,4,7), (2,5,8)] # col
    wins = {'X':0, 'O':0}
    for (i, j, k) in indexes:
        if (testcase[i]!='.') and (testcase[i] == testcase[j] == testcase[k]):
            wins[testcase[i]] += 1
    return wins

def isValid(testcase):
    c = Counter(testcase)
    wins = win(testcase)
    if c['O'] > c['X'] or (abs(c['O'] - c['X'])>1): # wrong case -> invalid!
        return 'invalid'
    if wins['X'] and wins['O'] and c['.']!=0: # both win -> invalid!
        return 'invalid'
    if wins['X'] and (c['X'] != c['O'] + 1): # 'X' wins but count wrong -> invalid!
        return 'invalid'
    if wins['O'] and (c['X'] != c['O']): # 'O' wins but count wrong -> invalid!
        return 'invalid'
    if wins['X'] or wins['O'] or c['.']==0: # 'X' or 'O' wins and count right! Or full -> valid 
        return 'valid'
    return 'invalid' # else invalid!

ans = []
while True:
    testcase = input()
    if testcase == 'end':
        break
    ans.append(isValid(list(testcase)))
print(*ans, sep='\n')