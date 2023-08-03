from Functions import Node, calc_v2, best_route, calculate_dis
from timeit import default_timer as timer
from collections import deque
import numpy as np



num_cit = 5
cities_lst = []
for i in range(num_cit):
    node = Node(i)
    node.get_position()
    node.get_connections(5, 100)
    cities_lst.append(node)

calculate_dis(cities_lst)
for i in cities_lst:
    i.show_param()


def dfs(city_map, start_point, path=None, path_lst=[]):
    if path is None:
        path = [start_point]

    if len(path) == len(city_map):
        path_lst.append(path)

    possible = city_map[start_point].neighbors
    for i in possible:
        if i not in path:
            new_path = path.copy()
            new_path.append(i)
            dfs(city_map, i, new_path, path_lst)

    return path_lst

start = timer()
dfs_paths = dfs(cities_lst, 0)
costs_dfs = calc_v2(cities_lst, dfs_paths)
end = timer()
time_dfs = end - start

def bfs(graph, start):
    queue = deque([(start, [start])])
    all_paths = []

    while queue:
        current_node, path = queue.popleft()

        if len(path) == len(graph):
            all_paths.append(path)
            continue

        for neighbor in graph[current_node].neighbors:
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return all_paths

start = timer()
bfs_paths = bfs(cities_lst, 0)
costs_bfs = calc_v2(cities_lst, bfs_paths, assimetrical=False)
end = timer()
time_bfs = end - start

### Wyniki
def best_route(costs, paths):
    min_cost = min(costs)
    for cost in range(len(costs)):
        if min_cost == costs[cost]:
            indx = cost
    return(min_cost, paths[indx])

print(f'Najkrótsza scieżka dla DFS oraz jej koszt: {best_route(costs_dfs, dfs_paths)} w czasie: {time_dfs}')
print(f'Najkrótsza scieżka dla BFS oraz jej koszt: {best_route(costs_bfs, bfs_paths)} w czasie: {time_bfs}')

