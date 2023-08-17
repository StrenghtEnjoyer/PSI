from functions import Node, calculate_cost, calc_v3, calculate_dis
from timeit import default_timer as timer
import numpy as np
import copy
import random
from zad3 import astar




num_cit = 4
cities_lst = []
for i in range(num_cit):
    node = Node(i)
    node.get_position()
    node.get_connections(num_cit, 100)
    cities_lst.append(node)

calculate_dis(cities_lst)
for city in cities_lst:
    city.add_dict()

'''for city in cities_lst:
    city.show_param()
'''
class Aoc:
    def __init__(self, city_map: list[Node], start_point: int, ants: int):
        self.start_point = start_point
        self.ants = ants
        self.city_map = city_map
        self.alpha = 2
        self.beta = 1
        self.pheromon_map = self.get_pheromon_map(city_map)
        self.path = [start_point]

    def get_pheromon_map(self, cities):
        pheromone_map = []
        for city in cities:
            pheromon_paths = {}
            for path in city.neighbors:
                pheromon_paths[path] = 1
            pheromone_map.append(pheromon_paths)
        return pheromone_map
     
    def choose_weighted_path(self):
        weights = []
        total_prob = 0.0
        avaiable_cities = []

        for path in self.city_map[self.path[-1]].neighbors:
            if path not in self.path:

                tau_ij = self.pheromon_map[self.path[-1]][path]
                eta_ij = 1.0 / self.city_map[self.path[-1]].dict[path]

                probability = (tau_ij ** self.alpha) * (eta_ij ** self.beta)
                weights.append(probability)
                avaiable_cities.append(path)
                total_prob += probability
        if len(weights) == 0:
            return self.start_point
        #weights = [prob / total_prob for prob in weights]
        chosen_path = random.choices(avaiable_cities, weights)
        return chosen_path[0]

    def vaporize(self):
        for path in self.pheromon_map:
            for node in path:
                path[node] *= 0.5
    
    def update_pheromone_map(self):
        self.pheromon_map[self.path[-2]][self.path[-1]] += self.city_map[self.path[-2]].dict[self.path[-1]]
        
    def get_path(self):
        for ant in range(self.ants):
            for i in range(len(self.city_map)):
                choice = self.choose_weighted_path()
                self.path.append(choice)
                self.update_pheromone_map()
                
            self.path=[self.start_point]
            self.vaporize()
        for i in range(len(self.city_map)):
                choice = self.choose_weighted_path()
                self.path.append(choice)
                self.update_pheromone_map()
        return(self.path)



aoc = Aoc(cities_lst, 0, 30)
zzz = aoc.get_path()
print(zzz)
#print(calc_v3(cities_lst,[zzz]))
#print(astar(0,0,cities_lst,1))
