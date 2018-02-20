from collections import namedtuple

Collection = namedtuple("Collection", ["value", "locations", "ranges"])


def read_file(filename):
    f = open(filename)

    lines = f.readlines()
    T = int(lines[0])
    S = int(lines[1])

    satellites = []
    line = 2
    for i in range(S):
        ps, ls, v, w, d = (int(i) for i in lines[line].split(" "))
        line = line + 1
        satellites.append((ps, ls, v, w, d))

    C = int(lines[S + 2])
    line = S + 3

    collections = []
    for l in range(C):
        V, L, R = (int(i) for i in lines[line].split(" "))
        c = Collection(V, [], [])
        line = line + 1
        for i in range(L):
            pi, li = (int(i) for i in lines[line + i].split(" "))
            c.locations.append((pi, li))
        line = line + L

        for i in range(R):
            ts, te = (int(i) for i in lines[line].split(" "))
            line = line + 1
            c.ranges.append((ts, te))
        collections.append(c)

    return T, satellites, collections