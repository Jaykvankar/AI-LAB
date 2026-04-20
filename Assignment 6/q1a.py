# ---------------- HEURISTIC ----------------
h = {
    "Boston":0,
    "Portland":107,
    "Providence":50,
    "New York":215,
    "Philadelphia":270,
    "Baltimore":360,
    "Syracuse":260,
    "Buffalo":400,
    "Pittsburgh":470,
    "Cleveland":550,
    "Columbus":640,
    "Detroit":610,
    "Indianapolis":780,
    "Chicago":860
}

# ---------------- GRAPH ----------------

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

# ---------------- NODE ----------------

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost


# ---------------- A* SEARCH ----------------

def a_star(start, goal):

    frontier = [Node(start)]
    reached = {start: 0}

    while frontier:

        # choose node with smallest f = g + h
        min_index = 0
        for i in range(1, len(frontier)):
            f1 = frontier[i].cost + h[frontier[i].state]
            f2 = frontier[min_index].cost + h[frontier[min_index].state]
            if f1 < f2:
                min_index = i

        node = frontier.pop(min_index)

        if node.state == goal:
            return node

        for (neighbor, edge_cost) in graph[node.state]:
            new_cost = node.cost + edge_cost

            if neighbor not in reached or new_cost < reached[neighbor]:
                print(f"Expanding node {neighbor} with cost {new_cost}")
                reached[neighbor] = new_cost
                frontier.append(Node(neighbor, node, new_cost))

    return None


# ---------------- PRINT PATH ----------------

def print_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


# ---------------- RUN ----------------

result = a_star("Syracuse", "Chicago")

if result:
    print("Path:", print_path(result))
    print("Total Cost:", result.cost)
else:
    print("No Path Found")