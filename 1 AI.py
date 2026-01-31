import heapq

goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x = (state[i][j] - 1) // 3
                y = (state[i][j] - 1) % 3
                dist += abs(i - x) + abs(j - y)
    return dist

def neighbors(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [list(row) for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            moves.append(tuple(tuple(row) for row in new))
    return moves

def solve(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal:
            return path + [state]
        visited.add(state)
        for n in neighbors(state):
            if n not in visited:
                heapq.heappush(pq, (g + 1 + manhattan(n), g + 1, n, path + [state]))

start_state = ((1, 2, 3),
               (4, 0, 6),
               (7, 5, 8))

solution = solve(start_state)

for step in solution:
    for row in step:
        print(row)
    print()
