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


    scores_per_endpoint = []
    for ie in range(simul.E):
        def compute_score(_c, _v, _ie):
            score = 0.
            _e = simul.endpoints[_ie]
            if _c in _e.caches:
                Lc = _e.caches[_c]
                endpoint_score = vid_score_per_ep[_ie]
                score += (_e.Ld - Lc) * endpoint_score.get(_v,0.)
            return score

        #print len(vid_score_per_ep[0].keys())
        #print len(vid_score_per_ep[0].keys())
        #print len(simul.endpoints[0].caches.keys())

        scores_per_endpoint += [
            (ie, c,v,compute_score(c,v, ie)) for v in vid_score_per_ep[ie].keys() for c in simul.endpoints[ie].caches.keys()
        ]
        #print "FIRST SCORE LIST"


        if ie % 10 == 0:
            print ie

    scores_per_endpoint = sorted(scores_per_endpoint, key=lambda x: -x[3])

    caches_spaces = dict((i,simul.X) for i in range(simul.C))
    cache_vids = dict((i,[]) for i in range(simul.C))
    endpoints_vids = dict((i,[]) for i in range(simul.E))

    for ie,c,v,score in scores_per_endpoint:
        vid_size = simul.video_sizes[v]
        videos_in_cache = cache_vids[c]
        if caches_spaces[c] >= vid_size and v not in videos_in_cache and v not in endpoints_vids[ie]:
            videos_in_cache.append(v)
            caches_spaces[c] -= vid_size
            endpoints_vids[ie].append(v)

    print cache_vids[0]
    print cache_vids[1]
    print cache_vids[simul.C - 1]