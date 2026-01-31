from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()

    # (amount in jug1, amount in jug2)
    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        # Check if target is achieved
        if a == target or b == target:
            print("Target achieved:", (a, b))
            return

        # All possible states
        states = [
            (jug1, b),        # Fill jug1
            (a, jug2),        # Fill jug2
            (0, b),           # Empty jug1
            (a, 0),           # Empty jug2
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),  # Pour jug1 → jug2
            (a + min(b, jug1 - a), b - min(b, jug1 - a))   # Pour jug2 → jug1
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("No solution found")

# Example
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

water_jug(jug1_capacity, jug2_capacity, target_amount)
