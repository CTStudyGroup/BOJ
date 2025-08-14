minkyum = input()

minimum = float('inf')
maximum = 0

def minkyum2Ten(minkyum):
    total = 1

    m_count = minkyum.count('M')
    k_count = minkyum.count('K') # 0 또는 1

    if(k_count == 0):
        total = 10**(m_count-1)
    else:
        total = 10**(m_count) * 5**(k_count)
    
    return total

def backtrack(index, arr, total):
    global minimum
    global maximum
    tmp = total[:]

    if(index == len(minkyum)):
        if(len(arr) != 0):
            tmp += str(minkyum2Ten(arr))
        
        minimum = min(int(tmp), minimum)
        maximum = max(int(tmp), maximum)
        return

    # 뒤로 계산을 넘기는 경우 (K는 반드시 잘라야 함)
    if (minkyum[index] != 'K'):
        arr.append(minkyum[index])
        backtrack(index + 1, arr, total)
        arr.pop(-1)
    
    # 여기서 자르고, 뒤에는 새로 시작하는 경우
    current = minkyum[index]
    before = arr[:]
    before.append(current)
    tmp = tmp + str(minkyum2Ten(before))

    total = tmp    
    arr = []
    backtrack(index + 1, arr, total)

backtrack(0, [], '')
print(int(maximum))
print(int(minimum))