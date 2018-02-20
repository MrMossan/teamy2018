from collections import namedtuple

Simulation = namedtuple("Simulation", ["V", "E", "R", "C", "X", "video_sizes", "endpoints", "requests"])
Endpoint = namedtuple("Endpoint", ["Ld", "caches"])
Request = namedtuple("Request", ["Rv", "Re", "Rn"])

def read_file(filename):
    f = open(filename)

    lines = f.readlines()

    V, E, R, C, X = (int(i) for i in lines[0].split(" "))

    video_sizes = [float(i) for i in lines[1].split(" ")]

    endpoints = []
    line = 2
    for i in range(E):
        Ld, caches_len = (int(i) for i in lines[line].split(" "))
        line += 1
        caches = dict()
        for j in range(caches_len):
            c, Lc = (int(i) for i in lines[line].split(" "))
            caches[c] = Lc
            line += 1
        endpoints.append(Endpoint(Ld, caches))
    requests = []
    for i in range(R):
        Rv, Re, Rn = (int(i) for i in lines[line].split(" "))
        line += 1
        requests.append(Request(Rv, Re, Rn))

    return Simulation(V,E,R,C,X, video_sizes, endpoints,requests)

def solve(simul):

    vid_score_per_ep = [
        dict()
        for e in simul.endpoints
    ]
    for r in simul.requests:
        vid_score_per_ep[r.Re][r.Rv] = r.Rn / simul.video_sizes[r.Rv]

    print "COMPUTED VID SCORE PER EP"

    def compute_score(_c, _v):
        score = 0.
        for ie, _e in enumerate(simul.endpoints):
            if _c in _e.caches:
                Lc = _e.caches[_c]
                endpoint_score = vid_score_per_ep[ie]
                score += (_e.Ld - Lc) * endpoint_score.get(_v,0.)
        return score

    score_per_vid_and_cache = [
        (c,v,compute_score(c,v)) for c in range(simul.C)
                    for v in range(simul.V)
    ]

    print "FIRST SCORE LIST"

    score_per_vid_and_cache = sorted(score_per_vid_and_cache, key=lambda x:x[2])

    print score_per_vid_and_cache[-1]