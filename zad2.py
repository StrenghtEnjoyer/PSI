from Functions import Node, calculate_cost, best_route
from timeit import default_timer as timer
import numpy as np
import math

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


for i in cities_lst:
    i.show_param()

def greed1(start, cities):
    path = [start]
    individual_costs = []
    cost = 0
    for i in range(len(cities)):
        city = cities[path[-1]]
        connections = city.neighbors
        distance = city.costs
        indexes_to_remove = []

        if len(path) == len(cities):
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

    last_dist = np.linalg.norm(cities[path[-1]].position - cities[path[0]].position)
    individual_costs.append(last_dist)
    return path, sum(individual_costs)

            
            
        
print(greed1(0, cities_lst))