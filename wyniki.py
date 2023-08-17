from functions import Node, calc_v3, calculate_dis
from zad1_new import bfs, dfs, best_route
from zad2 import greed1, greed2
from zad3 import astar
from zad4 import Aoc
from timeit import default_timer as timer
import numpy as np


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
### DFS / BFS

start = timer()
dfs_paths = dfs(cities_lst, 0)
costs_dfs = calc_v3(cities_lst, dfs_paths)
end = timer()
time_dfs = end - start

start = timer()
bfs_paths = bfs(cities_lst, 0)
costs_bfs = calc_v3(cities_lst, bfs_paths)
end = timer()
time_bfs = end - start

print(f'Najkrótsza scieżka dla DFS oraz jej koszt: {best_route(costs_dfs, dfs_paths)} w czasie: {time_dfs}')
print(f'Najkrótsza scieżka dla BFS oraz jej koszt: {best_route(costs_bfs, bfs_paths)} w czasie: {time_bfs}')

### A-star

start = timer()
a_star = astar(0, 0, cities_lst, 1)
end = timer()
time_astar = start - end

print(f'Najkrótsza ścieżka dla a* oraz jej koszt: {a_star} w czasie: {time_astar}')

### AOC 

start = timer()
aoc = Aoc(cities_lst, 0, 30)
aoc_path = aoc.get_path()
aoc_cost = calc_v3(cities_lst, [aoc_path])
end = timer()
time_aoc = start - end

print(f'Najkrótsza ścieżka dla aoc oraz jej koszt: {aoc_path, aoc_cost} w czasie: {time_aoc}')


### GREED

start = timer()
greed1_path = greed1(0, cities_lst)
cost_greed1 = calc_v3(cities_lst, [greed1_path])
end = timer()
time_greed1 = start - end

start = timer()
greed2_path = greed2(0, cities_lst)
cost_greed2 = calc_v3(cities_lst, [greed2_path])
end = timer()
time_greed2 = start - end

print(f'Najkrótsza ścieżka dla greed1 oraz jej koszt: {greed1_path, cost_greed1} w czasie: {time_greed1}')
print(f'Najkrótsza ścieżka dla greed2 oraz jej koszt: {greed2_path, cost_greed2} w czasie: {time_greed2}')

