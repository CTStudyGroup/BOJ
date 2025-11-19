import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

inorder = list(map(int, input().split()))

postorder = list(map(int, input().split()))

inorder_idx = {val : idx for idx, val in enumerate(inorder)}

preorder = []

def preorder_find(in_start, in_end, post_start, post_end):
    
    if in_start > in_end or post_start > post_end :
        return
    root = postorder[post_end]
    preorder.append(root)
    
    root_idx_inorder = inorder_idx[root]
    left_subtree_size = root_idx_inorder - in_start
    
    preorder_find (in_start, root_idx_inorder-1, post_start, post_start + left_subtree_size - 1)
    preorder_find(
        root_idx_inorder + 1,
        in_end,
        post_start + left_subtree_size,
        post_end - 1 )
    
preorder_find(0, N-1, 0, N-1)
print(*preorder)
