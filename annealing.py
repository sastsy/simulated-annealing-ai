import networkx as nx
import random
import math

def simulated_annealing_shortest_hamilton_cycle(graph, initial_temperature=1000, cooling_rate=0.95, iterations=2000):
    current_solution = list(graph.nodes())
    random.shuffle(current_solution)
    current_cost = calculate_hamilton_cycle_cost(graph, current_solution)
    temperature = initial_temperature

    best_solution = current_solution.copy()
    best_cost = current_cost

    for iteration in range(iterations):
        new_solution = current_solution.copy()
        swap_indices = sorted(random.sample(range(len(new_solution)), 2))
        new_solution[swap_indices[0]:swap_indices[1]+1] = reversed(new_solution[swap_indices[0]:swap_indices[1]+1])
        new_cost = calculate_hamilton_cycle_cost(graph, new_solution)

        cost_difference = new_cost - current_cost

        if cost_difference < 0 or random.random() < math.exp(-cost_difference / temperature):
            current_solution = new_solution
            current_cost = new_cost
            if current_cost < best_cost:
                best_solution = current_solution.copy()
                best_cost = current_cost

        temperature = initial_temperature * math.exp(-iteration / iterations * cooling_rate)

    return best_solution, best_cost

def calculate_hamilton_cycle_cost(graph, cycle):
    cost = 0
    for i in range(len(cycle)):
        if graph.has_edge(cycle[i], cycle[(i + 1) % len(cycle)]):
            cost += graph[cycle[i]][cycle[(i + 1) % len(cycle)]]['weight']
        else:
            return float('inf')
    return cost

# graph = nx.DiGraph()
# edges = [
#             (1, 2, 10),
#             (1, 3, 20),
#             (2, 3, 15),
#             (2, 4, 25),
#             (3, 4, 30),
#             (3, 5, 35),
#             (4, 5, 40),
#             (5, 1, 45)
#         ]

# graph.add_weighted_edges_from(edges)

# shortest_cycle, cycle_cost = simulated_annealing_shortest_hamilton_cycle(graph)

# print("Shortest Hamiltonian Cycle:", shortest_cycle)
# print("Cost:", cycle_cost)
