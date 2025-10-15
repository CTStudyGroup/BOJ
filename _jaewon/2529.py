from collections import defaultdict
k = int(input())
op = list(input().split())

hash = defaultdict(int)

for i in range(10):
    hash[i] = 1

def cal(before, index, number):
    if(op[index] == '<'):
        if(before < number):
            return True
        else:
            return False
    else:
        if(before > number):
            return True
        else:
            return False

result = []

def backtrack(before, index, path):
    global hash, result
    if(index == k):
        for number in hash:
            if(hash[number] == 1 and cal(before, index-1, number)):
                hash[number] -= 1
                path.append(str(number))
                result.append(''.join(path))
                hash[number] += 1
                path.pop(-1)
        return
               
        
    for number in hash:
        if(hash[number] == 1 and cal(before, index-1, number)):
            hash[number] -= 1
            path.append(str(number))
            backtrack(number, index + 1, path)
            hash[number] += 1
            path.pop(-1)

for start in range(10):
    hash[start] -= 1
    backtrack(start, 1, [str(start)])
    hash[start] += 1

result.sort()
print(result[-1])
print(result[0])


