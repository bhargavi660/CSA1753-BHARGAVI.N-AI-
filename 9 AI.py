from itertools import permutations

def tsp(graph):
    n = len(graph)
    cities = list(range(n))
    min_cost = float('inf')
    best_path = None

    for path in permutations(cities[1:]):
        cost = 0
        current = 0

        for city in path:
            cost += graph[current][city]
            current = city

        cost += graph[current][0]  # return to start

        if cost < min_cost:
            min_cost = cost
            best_path = (0,) + path + (0,)

    return min_cost, best_path


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp(graph)
print("Minimum Cost:", cost)
print("Best Path:", path)
