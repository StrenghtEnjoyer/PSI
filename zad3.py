from functions import Node, calculate_cost, calc_v3, calculate_dis
from timeit import default_timer as timer
import numpy as np
import copy




#print(list(cities_lst[0].dict.keys()))

def calc_step(cities, path):
    cost = 0
    for i in range(len(path)):
        a = path[i:i+2]
        
        if len(a) == 2:
            cost = cost + cities[a[0]].dict[a[1]]
            
    return cost





def astar(start, finish, cities, heur):
    all_values = []
    for i in [dis.costs for dis in cities]:
        for j in i:
            all_values.append(j)
    global_min = min(all_values)
    global_mean = np.mean(all_values)
    global_ = global_min
    if heur != 1:
        global_ = global_mean
    possible_paths = []
    path = [start]
    already_seen = []
    step_cost = 0
    
    while True:

        for item in cities[path[-1]].dict.items():
            if item[0] in path:
                continue

            a = path.copy()
            a.append(item[0])
            heuric_cost = item[1] + (len(cities) - len(a)) * global_ + step_cost
            step = (a, heuric_cost)

            if step in already_seen:
                continue

            possible_paths.append(step)

        min_heur_path = min(possible_paths, key=lambda x: x[1])
        already_seen.append(min_heur_path)
        path = min_heur_path[0]
        for paths in possible_paths:
            if path == paths[0]:
                step_cost = calc_step(cities, path)
                break
        possible_paths.remove(min_heur_path)

        if len(path) == len(cities):
            if finish in cities[path[-1]].dict.keys():
                path.append(finish)
                step_cost = calc_step(cities, path)
                step = (path, step_cost)
                possible_paths.append(step)
                min_heur_path = min(possible_paths, key=lambda x: x[1])
                already_seen.append(min_heur_path)
                path = min_heur_path[0]
                possible_paths.remove(min_heur_path)

            else:
                min_heur_path = min(possible_paths, key=lambda x: x[1])
                already_seen.append(min_heur_path)
                path = min_heur_path[0]
                possible_paths.remove(min_heur_path)

        if len(path) == len(cities) + 1:
            break

    return path, step_cost
        
    

#aaa = astar(0, 0, cities_lst, 1)
#print(aaa)

