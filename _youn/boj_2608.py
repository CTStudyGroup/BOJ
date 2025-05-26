def ROME_to_INT(ROME_num:str):
    ROME1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ROME2 = {'IV':4, 'IX':9, 'XL':40, 'XC': 90, 'CD':400, 'CM':900}

    INT_num = 0
    for k in ROME2.keys():
        if ROME_num.find(k)==-1: continue
        INT_num += ROME2[k]
        ROME_num = ROME_num.replace(k, '')
    INT_num += sum(map(lambda x: ROME1[x], ROME_num))
    return INT_num

def INT_to_ROME(INT_num:int):
    ROME = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', \
            90:'XC', 50:'L', 40: 'XL', 10:'X', 9:'IX', 5:'V',\
            4:'IV', 1:'I'}
    
    ROME_num = ''
    for k in ROME.keys():
        while INT_num >= k: 
            ROME_num += ROME[k]
            INT_num -= k
    return ROME_num

def solve():
    a = ROME_to_INT(input())
    b = ROME_to_INT(input())
    ans = [a+b, INT_to_ROME(a+b)]
    print(*ans, sep='\n')

solve()