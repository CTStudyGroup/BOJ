# 입력 받기
T = int(input())
arr = [input() for _ in range(T)]


def is_palindrome(s):
    for left in range(len(s)-1):
        right = len(s)-1-left
        if(s[left] != s[right]):
            return False
    return True


def is_pseudo_palindrome(s):
    for left in range(len(s)-1):
        right = len(s)-1-left
        if(s[left] != s[right]):  # 문자가 다른 지점이 생기면
            s_left = s[left+1:right+1]  # 왼쪽 문자 제거
            s_right = s[left:right]  # 오른쪽 문자 제거
            return is_palindrome(s_left) or is_palindrome(s_right)

    return False


for string in arr:
    if(is_palindrome(string)):
        print(0)
    elif(is_pseudo_palindrome(string)):
        print(1)
    else:
        print(2)
