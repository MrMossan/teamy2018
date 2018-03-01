from collections import namedtuple

Simulation = namedtuple("Simulation", ["R", "C", "F", "N", "B", "T", "requests"])
Ride = namedtuple("Ride", ["a", "b", "x", "y", "s", "f", "id"])
Position = namedtuple("Position", ["x", "y"])

def read_file(filename):
    f = open(filename)

    lines = f.readlines()

    R, C, F, N, B, T = (int(i) for i in lines[0].split(" "))

    rides = []
    line = 1
    for i in range(N):
        a, b, x, y, s, f = (int(i) for i in lines[line].split(" "))
        rides.append(Ride(a,b,x,y,s,f, line - 1))
        line += 1

    return Simulation(R,C,F,N,B,T,rides)

def request_dist(r):
    return abs(r.x-r.a) + abs(r.y - r.b)

def dist_req_end_to_other(lhs,rhs):
    return abs(lhs.x-rhs.a) + abs(lhs.y - rhs.b)

def assign_request(car, request, cars_availability, cars_position, assigned_requests, t):

    assigned_requests[car].append(request.id)

    cars_availability[car] = max(t + dist_req_end_to_other(cars_position[car], request), request.s) + request_dist(request)

    cars_position[car] = request


def solve(simul):

    assigned_requests = dict((car, []) for car in range(simul.F))

    chrono_reqs = sorted(simul.requests, key = lambda r: r.s)

    cars_availability = [0 for _ in range(simul.F)]

    cars_position = dict((car, Position(0,0)) for car in range(simul.F))

    for t in range(simul.T):

        chrono_reqs = [r for r in chrono_reqs if r.f - request_dist(r) >= t]

        for car, availability_time in enumerate(cars_availability):

            if availability_time <= t:

                reqs_for_car = [_r for _r in chrono_reqs if _r.f >= request_dist(_r) + dist_req_end_to_other(cars_position[car], _r) + t]

                if reqs_for_car:

                    best_request = min(reqs_for_car, key=lambda _r: dist_req_end_to_other(cars_position[car], _r))

                    assign_request(car, best_request, cars_availability, cars_position, assigned_requests, t)

                    chrono_reqs = [r for r in chrono_reqs if r.id != best_request.id]

    for car, requests in assigned_requests.items():
        print str(len(requests)) + " "  + " ".join(str(r) for r in requests)









