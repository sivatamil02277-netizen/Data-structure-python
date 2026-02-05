graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

# BFS
visited = []
queue = [1]

while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
        queue.extend(graph[node])

print("BFS Traversal:", visited)

# DFS
visited = []

def dfs(n):
    if n not in visited:
        visited.append(n)
        for i in graph[n]:
            dfs(i)

dfs(1)
print("DFS Traversal:", visited)
