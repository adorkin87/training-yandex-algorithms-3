from sys import setrecursionlimit


def dfs(graph, current_v, comp):
    list_visited[current_v] = True
    list_components[current_v] = comp
    for i in graph[current_v]:
        if not list_visited[i]:
            dfs(graph, i, comp)


setrecursionlimit(100000)
with open('input.txt', 'r') as f:
    source_array = f.readlines()
v, e = map(int, source_array.pop(0).split())
list_adjacency = [[]]
list_visited = [-1]
list_components = [-1]
for i in range(v):
    list_adjacency.append([])
    list_visited.append(False)
    list_components.append(-1)
for i in range(e):
    a, b = map(int, source_array[i].split())
    if a != b:
        list_adjacency[a].append(b)
        list_adjacency[b].append(a)
    else:
        list_adjacency[a].append(b)
comp = 1
for i in range(1, v + 1):
    if not list_visited[i]:
        dfs(list_adjacency, i, comp)
        comp += 1
list_components.pop(0)
set_components = set(list_components)
dict_components = dict.fromkeys(set_components, 0)
dict_components_value = dict_components.fromkeys(dict_components, '')
for i in range(1, v + 1):
    dict_components[list_components[i - 1]] += 1
    dict_components_value[list_components[i - 1]] += str(i) + ' '
dict_components = dict(sorted(dict_components.items(), key=lambda item: item[1], reverse=True))

print(len(set_components))
for key, value in dict_components.items():
    print(value)
    print(dict_components_value[key])
