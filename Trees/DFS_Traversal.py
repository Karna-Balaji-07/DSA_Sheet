# Level order traversal
from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def dfs(root):
    if root is None:
        return []

    q = deque()
    result = []
    q.append(root)
    level = 0
    while q:
        lenq = len(q)
        result.append([])
        for _ in range(lenq):
            node =q.popleft()
            result[level].append(node)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return result

