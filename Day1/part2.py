pos = 50
pass_zero = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        steps = int(line[1:])

        if direction == "R":
            first = 100 if pos == 0 else 100 - pos
        else:
            first = 100 if pos == 0 else pos

        if first <= steps:
            pass_zero += 1 + (steps - first) // 100

        # Update final position
        if direction == "R":
            pos = (pos + steps) % 100
        else:
            pos = (pos - steps) % 100

print(pass_zero)