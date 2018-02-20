from collections import namedtuple

Simulation = namedtuple("Simulation", ["V", "E", "R", "C", "X", "video_sizes", "endpoints", "requests"])
Endpoint = namedtuple("Endpoint", ["Ld", "caches"])
Cache = namedtuple("Cache", ["c" ,"Lc"])
Request = namedtuple("Request", ["Rv", "Re", "Rn"])

def read_file(filename):
    f = open(filename)

    lines = f.readlines()

    V, E, R, C, X = (int(i) for i in lines[0].split(" "))

    video_sizes = [int(i) for i in lines[1].split(" ")]

    endpoints = []
    line = 2
    for i in range(E):
        Ld, caches_len = (int(i) for i in lines[line].split(" "))
        line += 1
        caches = []
        for j in range(caches_len):
            c, Lc = (int(i) for i in lines[line].split(" "))
            caches.append(Cache(c,Lc))
            line += 1
        endpoints.append(Endpoint(Ld, caches))
    requests = []
    for i in range(R):
        Rv, Re, Rn = (int(i) for i in lines[line].split(" "))
        line += 1
        requests.append(Request(Rv, Re, Rn))

    return Simulation(V,E,R,C,X, video_sizes, endpoints,requests)
