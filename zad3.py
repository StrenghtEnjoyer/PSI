from functionsv1 import Node, calculate_cost, calc_v3, calculate_dis
from timeit import default_timer as timer
import numpy as np
import copy



num_cit = 5
cities_lst = []
for i in range(num_cit):
    node = Node(i)
    node.get_position()
    node.get_connections(num_cit, 100)
    cities_lst.append(node)

calculate_dis(cities_lst)
for city in cities_lst:
    city.add_dict()

for city in cities_lst:
    city.show_param()

#print(list(cities_lst[0].dict.keys()))

def astar(start, finish, cities):
    global_min = min(min([dis.costs for dis in cities_lst]))
    possible_paths = []
    path = [start]
    already_seen = []
    

    while True:
        
        for item in cities[path[-1]].dict.items():
            if item[0] in path:
                continue

            a = path.copy()
            a.append(item[0])
            heuric_cost = item[1] + (len(cities) - len(a)) * global_min
            step = (a, heuric_cost)
            if step in already_seen:
                continue
            possible_paths.append(step)

        min_heur_path = min(possible_paths, key=lambda x: x[1])
        already_seen.append(min_heur_path)
        path = min_heur_path[0]
        possible_paths.remove(min_heur_path)
        if len(path) == len(cities):
            if finish in cities[path[-1]].dict.keys():
                break
            else:
                min_heur_path = min(possible_paths, key=lambda x: x[1])
                already_seen.append(min_heur_path)
                path = min_heur_path[0]
                possible_paths.remove(min_heur_path)

    return path
        
    

aaa = astar(0, 0, cities_lst)
print(aaa)
print(calc_v3(cities_lst,[aaa]))

