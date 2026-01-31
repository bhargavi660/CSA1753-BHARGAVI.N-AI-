# Minimax Algorithm

def minimax(depth, is_max, values):
    if depth == 3:
        return values.pop(0)

    if is_max:
        return max(minimax(depth+1, False, values),
                   minimax(depth+1, False, values))
    else:
        return min(minimax(depth+1, True, values),
                   minimax(depth+1, True, values))


# Leaf node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

result = minimax(0, True, values)
print("Optimal value:", result)
