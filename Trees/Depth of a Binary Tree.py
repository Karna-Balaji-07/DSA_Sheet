# Depth of a binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def height(root):
    if root is None:
        return -1
    lheight = height(root.left)
    rheight = height(root.right)
    return max(lheight, rheight)+1

from collections import deque
def dfs(root):
    q = deque()
    result = []
    q.append(root)
    level = 0
    while q:
        lenq = len(q)
        result.append([])
        for i in range(lenq):
            node = q.popleft()
            result[level].append(node)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level +=1
    return level -1

