N = int(input())
string = input().strip()

# 포인터를 두개 두고, 오른쪽으로 한칸씩 이동하면서
# 새 칸의 알파벳이 현재 사용중인 알파벳이면 mx 업데이트
# 새 칸의 알파벳이 현재 사용중인 알파벳이 아니면 왼쪽 포인터를 사용중인 알파벳 개수가 N이하가 될 때까지 이동

left = 0
right = 0
mx = 1
_dict = {}
_dict[string[0]] = 1

while right < len(string)-1:
    right += 1
    _dict[string[right]] = _dict.get(string[right], 0) + 1  # 새 문자 추가

    while len(_dict) > N:
        _dict[string[left]] -= 1
        if _dict[string[left]] == 0:
            del _dict[string[left]]
        left += 1

    mx = max(mx, right-left+1)

print(mx)
