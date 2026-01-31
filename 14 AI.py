def alphabeta(d, maxp, v, a, b):
    if d == 3:
        return v.pop(0)

    if maxp:
        for _ in range(2):
            a = max(a, alphabeta(d+1, False, v, a, b))
            if b <= a: break
        return a
    else:
        for _ in range(2):
            b = min(b, alphabeta(d+1, True, v, a, b))
            if b <= a: break
        return b


values = [3, 5, 2, 9, 12, 5, 23, 23]
print("Optimal value:", alphabeta(0, True, values, -999, 999))
