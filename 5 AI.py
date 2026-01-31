from collections import deque

def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False

    if (M_left > 0 and M_left < C_left):
        return False
    if (M_right > 0 and M_right < C_right):
        return False

    return True


def get_successors(state):
    successors = []
    M_left, C_left, boat = state

    moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]

    for m, c in moves:
        if boat == 0:  # Left to Right
            new_state = (M_left - m, C_left - c, 1)
        else:          # Right to Left
            new_state = (M_left + m, C_left + c, 0)

        if is_valid(new_state):
            successors.append(new_state)

    return successors


def bfs():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for successor in get_successors(state):
            queue.append((successor, path + [successor]))

    return None


solution = bfs()

print("Solution Path:")
for step in solution:
    print(step)
