# 도둑이 연속된 M개의 집에서 각 집에서 보관중인 돈을 전부 훔침
# 만약 마을에서 K 원 이상의 돈을 훔치면 잡힘. (총 돈은 K 미만)
# N : 마을을 이루고 있는 집의 개수, M : 훔쳐야 할 연속된 집의 개수
# K : K 미만의 돈을 훔쳐야 함. 
# 입력 : T (test case)
        # N, M, K
        # N개의 집에서 각각 보관중인 돈이 시계방향 순서로
# 출력 : M개의 연속된 집을 고르는 방법의 수

# 시간 복잡도 : N < 100,000 , 1초 : O(N log N) :정렬, 힙, 트리 아래로 가능 
T = int(input())
for t in range(T) :
    N, M, K = map(int, input().split())
    stealing_plan = []
    board = list(map(int, input().split()))
    if N == M :
        if sum(board) < K :
            print(1)
            continue
    
    
    
    
    
    stealing_plan.append(sum(board[:M]))
    if stealing_plan[0] < K :
        count = 1
    else :
        count =0
    for idx in range(1, len(board)) :
        tmp = stealing_plan[idx-1] - board[idx-1] + board[(idx+M-1)%N]
        stealing_plan.append(tmp)
        if tmp < K :
            count += 1
    # print(stealing_plan)
    print(count)
