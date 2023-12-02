# imports go here


def parse_line(tokens):
    l_d = []
    for draws in tokens:
        d = {"r": 0, "b": 0, "g": 0}
        for entries in draws:
            match (entries[1]):
                case "blue":
                    d["b"] = int(entries[0])
                case "red":
                    d["r"] = int(entries[0])
                case "green":
                    d["g"] = int(entries[0])
        l_d.append(d)
    return l_d


def is_possible(l_d):
    dic_threshold = {"r": 12, "g": 13, "b": 14}
    for i in range(len(l_d)):
        dic = l_d[i]
        for k in dic_threshold.keys():
            if dic[k] > dic_threshold[k]:
                return False
    return True


def max_colors(l_d):
    dic_max = {"r": 0, "g": 0, "b": 0}
    for d in l_d:
        for k in d.keys():
            if d[k] > dic_max[k]:
                dic_max[k] = d[k]
    return dic_max


def lex_line(li):
    striped = li.split(":")[1]
    game_subsets = striped.split(";")
    for i in range(len(game_subsets)):
        game_subsets[i] = game_subsets[i].split(",")
        for j in range(len(game_subsets[i])):
            game_subsets[i][j] = game_subsets[i][j].split()
    return game_subsets


with open(f"inputs/day2", "r") as f:
    s = 0
    for i, l in enumerate(f.readlines()):
        l_d = parse_line(lex_line(l[:-1]))
        mini = max_colors(l_d)
        s += mini["r"] * mini["g"] * mini["b"]
    print(s)

