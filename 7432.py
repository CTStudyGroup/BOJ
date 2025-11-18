def insert_path(root, path) :
    dir_comp = path.strip().split("\\")
    
    cur = root
    for comp in dir_comp :
        if comp not in cur :
            cur[comp] = {}
        cur = cur[comp]
    
def print_tree(node, depth) :
    sorted_child_names = sorted(node.keys())
    
    for name in sorted_child_names : 
        child_node = node[name]
        indentation  = ' '*depth
        print(f"{indentation}{name}")
    
        print_tree(child_node, depth + 1)
        
def solve() :
    N = int(input())
    root = {}
    
    for _ in range(N) :
        path = input().strip()
        if path :
            insert_path(root, path)
    print_tree(root, 0)
    
solve()
