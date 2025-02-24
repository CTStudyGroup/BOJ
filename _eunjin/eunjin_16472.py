N = int(input())
string = input().strip()

# 포인터를 두개 두고, 오른쪽으로 한칸씩 이동하면서
# 새 칸의 알파벳이 현재 사용중인 알파벳이면 mx 업데이트
# 새 칸의 알파벳이 현재 사용중인 알파벳이 아니면 왼쪽 포인터를 사용중인 알파벳 개수가 N이하가 될 때까지 이동

left = 0
right = 0
mx = 1
x = 1
alphabet = [string[0]]

while right < len(string)-1:
    right += 1
    if string[right] in alphabet:
        x += 1
        mx = max(mx, x)
        alphabet.append(string[right])
    else:
        alphabet.append(string[right])
        while len(alphabet) > N:
            alphabet.remove(string[left])
            left += 1
        x = right-left+1
    # print("left:", left, ", right:", right, "x:", x, ", mx:", mx)

print(mx)
