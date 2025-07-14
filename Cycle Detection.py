# cycle detection using DFS Directed / Undirected graph
# Cycle detection using BFS Directed / Undirected graph

def cycleUtil(adjacent,node, visited, rec):
    if rec[node]:
        return True

    if visited[node]:
        return False

    visited[node] = True
    rec[node] = True

    for v in adjacent[node]:
        if cycleUtil(adjacent,v,visited,rec):
            return True


    rec[node] = False
    return False



