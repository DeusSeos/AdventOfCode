with open('input.txt') as f:
    accum = 0
    # should be only one line
    line = f.readline()
    ranges = line.split(",")
    for range in ranges:
        range.split("-", 2)
        for num in range(start, end):

