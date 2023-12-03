# imports go here
from numpy import prod


def is_reachable(m, x, y):
    return 0 <= x < len(m) and 0 <= y < len(m[x])


def reachable_cells(m, i, j):
    l = []
    d = {}
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if is_reachable(m, x, y) and m[x][y].isdigit() and not d.get((x, y)):
                l.append(parse_number(m, d, x, y))
    return l


def parse_number(m, d, x, y):
    num = ""
    start_pos = y
    while y < len(m[x]) and m[x][y].isdigit():
        num += m[x][y]
        d[(x, y)] = True
        y += 1
    y = start_pos - 1
    while y >= 0 and m[x][y].isdigit():
        num = m[x][y] + num
        d[(x, y)] = True
        y -= 1
    return int(num)


with open(f"inputs/day3", "r") as f:
    m = []
    visited = {}
    for l in f.readlines():
        print(list(l[:-1]))
        m.append(list(l[:-1]))
    s = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "*":
                c = reachable_cells(m, i, j)
                if len(c) == 2:
                    s += prod(c)
    print(s)
