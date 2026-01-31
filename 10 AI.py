def a_star(graph, h, start, goal):
    open_list = {start}
    closed_list = set()

    g = {start: 0}
    parent = {start: None}

    while open_list:
        current = min(open_list, key=lambda x: g[x] + h[x])

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        open_list.remove(current)
        closed_list.add(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            new_g = g[current] + cost
            if neighbor not in open_list or new_g < g.get(neighbor, float('inf')):
                g[neighbor] = new_g
                parent[neighbor] = current
                open_list.add(neighbor)

    return None


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

path = a_star(graph, heuristic, 'A', 'F')
print("Path found:", path)
