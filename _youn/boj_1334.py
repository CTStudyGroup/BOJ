def reverseN(ans):
    mid = (len(ans)+1)//2    
    for idx1 in range(mid):
        idx2 = len(ans)-idx1-1
        ans[idx2] = ans[idx1]
    return ans

def palindrome(n):
    ans = reverseN(list(n))
    if int(''.join(ans)) > int(n): return ''.join(ans)

    ans = list(n)
    mid = (len(ans)+1)//2

    if ans[mid-1]=='9':
        tmp = int(n) + 10**(len(ans)-mid)
        ans = list(str(tmp))
    else:
        ans[mid-1] = str(int(ans[mid-1])+1)

    reverseN(ans)
    return ''.join(ans)

N = input()
print(palindrome(N))