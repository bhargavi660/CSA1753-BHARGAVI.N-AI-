from itertools import permutations

def solve_crypt_arithmetic():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading letters should not be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        SEND = (mapping['S'] * 1000 +
                mapping['E'] * 100 +
                mapping['N'] * 10 +
                mapping['D'])

        MORE = (mapping['M'] * 1000 +
                mapping['O'] * 100 +
                mapping['R'] * 10 +
                mapping['E'])

        MONEY = (mapping['M'] * 10000 +
                 mapping['O'] * 1000 +
                 mapping['N'] * 100 +
                 mapping['E'] * 10 +
                 mapping['Y'])

        if SEND + MORE == MONEY:
            print("Solution Found!")
            print("SEND =", SEND)
            print("MORE =", MORE)
            print("MONEY =", MONEY)
            print("Mapping:", mapping)
            return

    print("No solution found")

# Run the program
solve_crypt_arithmetic()
