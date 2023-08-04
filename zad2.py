from functionsv1 import Node, calculate_cost, calc_v2
from timeit import default_timer as timer
import numpy as np
import math
import heapq

num_cit = 5
cities_lst = []
for i in range(num_cit):
    node = Node(i)
    node.get_position()
    node.get_connections(5, 100)
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

def greed1(start, cities):
    cities_copy = cities
    path = [start]
    individual_costs = []
    cost = 0
    for i in range(len(cities_copy)):
        city = cities_copy[path[-1]]
        connections = city.neighbors
        distance = city.costs
        indexes_to_remove = []

        if len(path) == len(cities_copy):
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
    return path, calc_v2(cities, [path])

        
       

def primm(start, cities):
    distances = [dis.costs for dis in cities]
    
    for i in range(len(distances)):
        distances[i].insert(i, 0)

    INF = 9999999
    V = len(distances)
    selected = []
    for i in range(len(distances)):
        selected.append(start)

    no_edge = 0
    selected[0] = True
    route = [start]
    costs = 0
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and distances[i][j]):  
                        if minimum > distances[i][j]:
                            minimum = distances[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(distances[x][y]))
        route.append(y)
        costs = costs + distances[x][y]
        selected[y] = True
        no_edge += 1
    plus = np.linalg.norm(cities_lst[route[-1]].position - cities_lst[start].position)
    costs = costs + plus
    calculate_dis(cities_lst)
    return route
   
start = timer()
primm_paths = primm(0, cities_lst)
costs_primm = calc_v2(cities_lst, [primm_paths])
end = timer()
time_primm = end - start
print(f'Najkrótsza scieżka dla primm oraz jej koszt: {primm_paths, costs_primm} w czasie: {time_primm}')

start = timer()
greed_paths = greed1(0, cities_lst)
end = timer()
time_greed = end - start
print(f'Najkrótsza scieżka dla primm oraz jej koszt: {greed_paths[0], greed_paths[1]} w czasie: {time_greed}')