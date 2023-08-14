import numpy as np
import random
from timeit import default_timer as timer
from collections import deque

random.seed(222720)

class Node:
    def __init__(self, id):
        self.id = id
        self.position = None
        self.neighbors = None
        self.costs = None
        self.dict = None

    def show_param(self):
        print(self.id, self.position, self.neighbors, self.costs, self.dict)

    def get_position(self):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        z = random.randint(0, 50)
        self.position = np.asarray([x, y, z])
    
    def get_connections(self, num_cit, possibility):
        con = []
        for i in range(num_cit):
            if i == self.id:
                pass
            else:
                a = random.randint(1, 100)
                if a <= possibility:
                    con.append(i)
        self.neighbors = con
    
    def add_costs(self, cost):
        self.costs = cost

    def add_dict(self):
        self.dict = dict(zip(self.neighbors, self.costs))


def calculate_cost(routes, cities, assimetrial=False):
    costs = []
    window = 2
    if assimetrial == False:
        for route in routes:
            cost = 0
            for i in range(len(route)):
                if route[i] == route[-1]:
                    cost = cost + np.linalg.norm(cities[route[-1]].position - cities[route[0]].position)
                    costs.append(cost)   
                else:
                    for j in range(len(route)):
                        a = route[j:j+window]
                        if len(a) == 2:
                            cost = cost + np.linalg.norm(cities[a[0]].position - cities[a[1]].position) 
        return costs
    elif assimetrial != False:
        for route in routes:
            cost = 0
            for i in range(len(route)):
                if route[i] == route[-1]:
                    direction = cities[route[-1]].position[2] - cities[route[0]].position[2]
                    if direction > 0 or direction < cities[route[-1]].position[2]:
                        cost = cost + (np.linalg.norm(cities[route[-1]].position - cities[route[0]].position)-np.linalg.norm(cities[route[-1]].position - cities[route[0]].position)*0.1)
                        costs.append(cost)   
                    else: 
                        cost = cost + (np.linalg.norm(cities[route[-1]].position - cities[route[0]].position)+np.linalg.norm(cities[route[-1]].position - cities[route[0]].position)*0.1)
                        costs.append(cost)  
                else:
                    for j in range(len(route)):
                        a = route[j:j+window]
                        if len(a) == 2:
                            direction = cities[a[0]].position[2] - cities[a[1]].position[2]
                            if direction > 0 or direction < cities[0].position[2]:
                                cost = cost + (np.linalg.norm(cities[a[0]].position - cities[a[1]].position)-np.linalg.norm(cities[a[0]].position - cities[a[1]].position)*0.1) 
                            else:
                                cost = cost + (np.linalg.norm(cities[a[0]].position - cities[a[1]].position)+np.linalg.norm(cities[a[0]].position - cities[a[1]].position)*0.1)
        return costs
    
def best_route(costs, paths):
    min_cost = min(costs)
    for cost in range(len(costs)):
        if min_cost == costs[cost]:
            indx = cost
    return(min_cost, paths[indx])

def calculate_dis(cities):
    for city in cities:
        costs = []
        position = city.position
        connections = city.neighbors
        for i in connections:
            cost = np.linalg.norm(position - cities[i].position)
            costs.append(cost)
        city.add_costs(costs)

def calc_v2(cities, paths, assimetrical=False):
    costs = []
    if assimetrical == False:
        for path in paths:
            cost = 0
            for i in range(len(path)):
                a = path[i:i+2]
                
                if len(a) == 2:
                    cost = cost + cities[a[0]].costs[cities[a[0]].neighbors.index(a[1])]

                if len(a) == 1:
                    cost = cost + cities[a[0]].costs[cities[a[0]].neighbors.index(path[0])]
                    costs.append(cost)
    else:
        for path in paths:
            if len(path) ==5:
                cost = 0
                for i in range(len(path)):
                    a = path[i:i+2]

                    if len(a) == 2:
                        wyn = cities[a[0]].costs[cities[a[0]].neighbors.index(a[1])]
                        direction = cities[a[0]].position[2] - cities[a[1]].position[2]

                        if direction > 0 or direction < cities[a[0]].position[2]:
                            cost = cost + (wyn - wyn*0.1)
                            
                        else:
                            cost = cost + (wyn + wyn*0.1)
                        
                    if len(a) == 1:
                        wynf = cities[a[0]].costs[cities[a[0]].neighbors.index(path[0])]
                        direction = cities[a[0]].position[2] - cities[path[0]].position[2]

                        if direction > 0 or direction < cities[a[0]].position[2]:
                            cost = cost + (wynf - wynf*0.1)
                            
                        else:
                            cost = cost + (wyn + wyn*0.1)
                        costs.append(cost)
    return costs

def calc_v3(cities, paths, assimetrical=False):
    costs = []
    if assimetrical == False:
        for path in paths:
            cost = 0
            for i in range(len(path)):
                a = path[i:i+2]
                
                if len(a) == 2:
                    cost = cost + cities[a[0]].dict[a[1]]
                if len(a) == 1:
                    if a[0] == path[0]:
                        costs.append(cost)
                        break
                    if path[0] in list(cities[a[0]].dict.keys()):  
                        cost = cost + cities[a[0]].dict[path[0]]
                        costs.append(cost)
                    else:
                        costs.append(float('inf'))
    if assimetrical != False:
        for path in paths:
            cost = 0
            for i in range(len(path)):
                a = path[i:i+2]
                
                if len(a) == 2:
                    direction = cities[a[0]].position[2] - cities[a[1]].position[2]
                    if direction > 0 or direction < cities[a[0]].position[2]:
                        cost = cost + (cities[a[0]].dict[a[1]]-cities[a[0]].dict[a[1]]*0.1)
                    else:
                        cost = cost + (cities[a[0]].dict[a[1]]+cities[a[0]].dict[a[1]]*0.1)
                if len(a) == 1:
                    if a[0] == path[0]:
                        break
                    if path[0] in list(cities[a[0]].dict.keys()): 
                        direction = cities[a[0]].position[2] - cities[path[0]].position[2] 
                        if direction > 0 or direction < cities[a[0]].position[2]:
                            cost = cost + (cities[a[0]].dict[path[0]]-cities[a[0]].dict[path[0]]*0.1)
                        else:
                            cost = cost + (cities[a[0]].dict[path[0]]+cities[a[0]].dict[path[0]]*0.1)
                        costs.append(cost)
                    else:
                        costs.append(float('inf'))
    return costs

