# ----- NODE -----

class Node:
    def __init__(self, STATE, PARENT=None, PATH_COST=0):
        self.STATE = STATE
        self.PARENT = PARENT
        self.PATH_COST = PATH_COST


# ----- FRONTIER CLASS -----

class Frontier:
    def __init__(self):
        self.frontier = []

    def IS_EMPTY(self):
        return len(self.frontier) == 0

    def ADD(self, node):
        self.frontier.append(node)

    def POP(self, f):
        min_index = 0
        for i in range(1, len(self.frontier)):
            if f(self.frontier[i]) < f(self.frontier[min_index]):
                min_index = i
        return self.frontier.pop(min_index)


# ----- GRAPH -----

graph = {
    "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
    "Detroit": [("Chicago", 283), ("Cleveland", 169), ("Buffalo", 256)],
    "Cleveland": [("Detroit", 169), ("Pittsburgh", 134), ("Columbus", 144), ("Chicago", 345), ("Buffalo", 189)],
    "Columbus": [("Cleveland", 144), ("Indianapolis", 176), ("Pittsburgh", 185)],
    "Indianapolis": [("Chicago", 182), ("Columbus", 176)],
    "Pittsburgh": [("Cleveland", 134), ("Buffalo", 215), ("Philadelphia", 305), ("Columbus", 185), ("Baltimore", 247)],
    "Buffalo": [("Detroit", 256), ("Pittsburgh", 215), ("Syracuse", 150), ("Cleveland", 189)],
    "Syracuse": [("Buffalo", 150), ("New York", 254), ("Boston", 312), ("Philadelphia", 253)],
    "New York": [("Syracuse", 254), ("Philadelphia", 97), ("Boston", 215), ("Providence", 181)],
    "Philadelphia": [("New York", 97), ("Pittsburgh", 305), ("Baltimore", 101), ("Syracuse", 253)],
    "Baltimore": [("Philadelphia", 101), ("Pittsburgh", 247)],
    "Boston": [("Syracuse", 312), ("Providence", 50), ("New York", 215), ("Portland", 107)],
    "Providence": [("Boston", 50), ("New York", 181)],
    "Portland": [("Boston", 107)]
}


# ----- PROBLEM -----

class Problem:
    def __init__(self, INITIAL, goal):
        self.INITIAL = INITIAL
        self.goal = goal

    def IS_GOAL(self, STATE):
        return STATE == self.goal


# ----- EXPAND -----

def EXPAND(problem, node):
    children = []
    for (s_prime, cost) in graph[node.STATE]:
        child = Node(
            STATE=s_prime,
            PARENT=node,
            PATH_COST=node.PATH_COST + cost
        )
        children.append(child)
    return children


# ----- BEST FIRST SEARCH -----

def BEST_FIRST_SEARCH(problem, f):

    node = Node(problem.INITIAL)

    frontier = Frontier()
    frontier.ADD(node)

    reached = {}
    reached[node.STATE] = node

    while not frontier.IS_EMPTY():

        node = frontier.POP(f)

        if problem.IS_GOAL(node.STATE):
            return node

        for child in EXPAND(problem, node):

            s = child.STATE

            if (s not in reached) or (child.PATH_COST < reached[s].PATH_COST):
                reached[s] = child
                frontier.ADD(child)

    return "failure"


# ----- f FUNCTION -----

def f(node):
    return node.PATH_COST


# ----- RUN -----

problem = Problem("Syracuse", "Chicago")
solution = BEST_FIRST_SEARCH(problem, f)


# ----- PRINT PATH -----

def print_path(node):
    path = []
    while node:
        path.append(node.STATE)
        node = node.PARENT
    return path[::-1]


if solution != "failure":
    print("Path:", print_path(solution))
    print("Total Cost:", solution.PATH_COST)
else:
    print("Failure")
