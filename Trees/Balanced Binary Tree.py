# Determine if the binary tree is height-balanced

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def balanced(root):
    def dfs(node):
        if node is None:
            return 0
        
        print(f'Visiting Node: {node.data}')  # Print current node
        
        left = dfs(node.left)
        print(f'Node {node.data} -> Left Height: {left}')
        if left == -1:
            return -1
        
        right = dfs(node.right)
        print(f'Node {node.data} -> Right Height: {right}')
        if right == -1:
            return -1
        
        diff = abs(left - right)
        print(f'Node {node.data} -> Height Difference: {diff}')
        
        if diff > 1:
            print(f'Node {node.data} is unbalanced!')
            return -1
        
        height = max(left, right) + 1
        print(f'Node {node.data} -> Computed Height: {height}')
        return height
    
    return dfs(root) != -1


from collections import deque
def build_tree(values):
    if not values or values[0] is None:
        return None
    
    root = Node(values[0])
    q = deque([root])
    i = 1
    
    while q and i < len(values):
        current = q.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            current.left = Node(values[i])
            q.append(current.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            current.right = Node(values[i])
            q.append(current.right)
        i += 1
    
    return root


values = [3, 9, 20, None, None, 15, 7]
root = build_tree(values)
print(balanced(root))

