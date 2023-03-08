from sys import setrecursionlimit


def dfs(graph, current_v):
    list_visited[current_v] = True
    for i in graph[current_v]:
        if not list_visited[i]:
            dfs(graph, i)


setrecursionlimit(2000)
with open('input.txt', 'r') as f:
    source_array = f.readlines()
v, e = map(int, source_array.pop(0).split())
list_adjacency = [[]]
list_visited = [-1]
for i in range(v):
    list_adjacency.append([])
    list_visited.append(False)
for i in range(e):
    a, b = map(int, source_array[i].split())
    if a != b:
        list_adjacency[a].append(b)
        list_adjacency[b].append(a)
    else:
        list_adjacency[a].append(b)
dfs(list_adjacency, 1)
result = []
for j in range(len(list_visited)):
    if list_visited[j] == True:
        result.append(j)
result.sort()
print(len(result))
print(*result)
