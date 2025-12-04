
with open("input.txt") as f:
    index = 50
    occur_zero = 0
    for line in f:
        direction, steps = line[:1], int(line[1:].rstrip())
        if direction == "L":
            index -= steps
            # print(index)
            while index < 0:
                index += 100
        else:
            index += steps
            while index > 99:
                index -= 100
        if index == 0:
            occur_zero += 1

    print(occur_zero)

