import sys

input = sys.stdin.readline
prime_nums = set([2, 3, 5])
def is_prime(number) :
    global prime_nums
    if number in prime_nums :
        return True
    if number % 2 == 0 : 
        return False
    for i in range(3, int(number**0.5)+1, 2):
        if number % i == 0:
            return False
    prime_nums.add(number)
    return True

def dfs(num, path) :
    if len(path) == 3 :
        if num == 0 :
            print(*path)
            return True
        return False
    
    for i in range(2, num+1) :
        if is_prime(i) :
            path.append(i)
            if dfs(num - i, path) :
                return True
            path.pop()
    return False

def get_prime_additions(number) :
    if not dfs(number, []) :
        print(0)
    
T = int(input())
for _ in range(T) :
    K = int(input())
    get_prime_additions(K)
    
    
