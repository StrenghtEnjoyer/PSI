from functions import Node, calculate_cost, calc_v3
from timeit import default_timer as timer
import numpy as np
import math
import heapq
from copy import copy

num_cit = 5
cities_lst = []
for i in range(num_cit):
    node = Node(i)
    node.get_position()
    node.get_connections(5, 80)
    cities_lst.append(node)

def calculate_dis(cities):
    for city in cities:
        costs = []
        position = city.position
        connections = city.neighbors
        for i in connections:
            cost = np.linalg.norm(position - cities[i].position)
            costs.append(cost)
        city.add_costs(costs)
    
    
calculate_dis(cities_lst)
for city in cities_lst:
    city.add_dict()

for city in cities_lst:
    city.show_param()


def greed1(start, cities):
    cities_copy = cities.copy()
    path = [start]
    individual_costs = []
    cost = 0
    for i in range(len(cities_copy)):
        city = cities_copy[path[-1]]
        connections = city.neighbors
        distance = city.costs
        indexes_to_remove = []

        if len(path) == len(cities_copy):
                if start in connections:
                    path.append(start)
                    break
                

        
        for j in path:
            if j in connections:
                indexes_to_remove.append(connections.index(j))
            if j in connections:
                connections.remove(j)

        if len(connections) != 4:
            for l in indexes_to_remove:
                distance.pop(l)

        individual_costs.append(min(distance))
        path.append(connections[distance.index(min(distance))])

    last_dist = np.linalg.norm(cities_copy[path[-1]].position - cities_copy[path[0]].position)
    individual_costs.append(last_dist)
    return path, calc_v3(cities, [path])

#greed_paths = greed1(0, cities_lst)
#print(greed_paths)

def greed2(start, cities):
    path=[start]
    cannot_go_back = []
    costs = []
    while True:
        con_and_val = list(cities[path[-1]].dict.items()).copy()
        xd = []
        for i in con_and_val:
            if i[0] not in path:
                xd.append(i)
        for i in con_and_val:
            if i[0] in cannot_go_back:
                xd.remove(i)
        
        min_con_and_val = min(xd, key=lambda x: x[1])
        path.append(min_con_and_val[0])
        costs.append(min_con_and_val[1])
        if len(path) == len(cities):
            if path[-1] in cities[path[-1]].dict.keys():
                break
            path[-1], path[-2] = path[-2], path[-1]
            break
    return path

aaa = greed2(0, cities_lst)
print(aaa)
print(calc_v3(cities_lst, [aaa]))