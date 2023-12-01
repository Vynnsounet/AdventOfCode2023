import re

with open("inputs/day1_2.txt") as f:
    s = 0
    l = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in f.readlines():
        for e in l:
            line = line.replace(e, e + str(l.index(e) + 1) + e)
        m = re.findall("[0-9]", line)
        s += int(m[0] + m[-1])
    print(s)
