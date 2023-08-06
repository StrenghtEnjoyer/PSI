import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to this node
        self.h = h  # Heuristic value (estimated cost to goal node)

    def f(self):
        return self.g + self.h

def neighbors_func(node, graph):
    neighbors, edge_costs = graph[node.state]
    return [(neighbor, cost) for neighbor, cost in zip(neighbors, edge_costs)]

def heuristic_func(state, goal_state, graph):
    # In this example, we will use the straight-line distance as the heuristic.
    x1, y1 = graph[state][0][0], graph[state][0][1]
    x2, y2 = graph[goal_state][0][0], graph[goal_state][0][1]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def astar(start, goal, graph):
    open_list = []
    closed_set = set()

    # Add the start node to the open list
    heapq.heappush(open_list, (start.f(), start))

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.state == goal.state:
            # Reconstruct the path from the goal node to the start node
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor_state, edge_cost in neighbors_func(current_node, graph):
            neighbor_node = Node(neighbor_state)
            if neighbor_node.state in closed_set:
                continue

            tentative_g = current_node.g + edge_cost

            if neighbor_node not in [node for _, node in open_list] or tentative_g < neighbor_node.g:
                neighbor_node.parent = current_node
                neighbor_node.g = tentative_g
                neighbor_node.h = heuristic_func(neighbor_node.state, goal.state, graph)

                # Add the neighbor node to the open list regardless of the current cost
                heapq.heappush(open_list, (neighbor_node.f(), neighbor_node))

    return None  # No path found

# Example usage:
graph = {
    0: [[1, 2, 3, 4], [28.30194339616981, 77.14920608794364, 223.6626924634504, 45.67274898667694]],
    1: [[0, 2, 3, 4], [28.30194339616981, 97.16480844420988, 246.30468935852602, 30.805843601498726]],
    2: [[0, 1, 3, 4], [77.14920608794364, 97.16480844420988, 149.85659811966906, 87.39565206576354]],
    3: [[0, 1, 2, 4], [223.6626924634504, 246.30468935852602, 149.85659811966906, 236.05296015936761]],
    4: [[0, 1, 2, 3], [45.67274898667694, 30.805843601498726, 87.39565206576354, 236.05296015936761]]
}

start_node = Node(0)  # Assuming starting node is 0
goal_node = Node(3)   # Assuming goal node is 3
path = astar(start_node, goal_node, graph)
print(path)

