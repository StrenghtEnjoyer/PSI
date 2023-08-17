from functions import Node, calc_v3, best_route, calculate_dis
from timeit import default_timer as timer
from collections import deque
import numpy as np





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



### Wyniki
def best_route(costs, paths):
    min_cost = min(costs)
    for cost in range(len(costs)):
        if min_cost == costs[cost]:
            indx = cost
    return(min_cost, paths[indx])



