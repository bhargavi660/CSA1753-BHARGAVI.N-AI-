def vacuum_cleaner():
    room = {'A':1, 'B':1}   # 1 = Dirty, 0 = Clean
    pos = 'A'

    while room['A'] or room['B']:
        if room[pos] == 1:
            print(f"Cleaning room {pos}")
            room[pos] = 0
        else:
            pos = 'B' if pos == 'A' else 'A'
            print(f"Moving to room {pos}")

    print("Both rooms are clean")

vacuum_cleaner()
