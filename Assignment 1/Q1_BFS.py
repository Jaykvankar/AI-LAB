from collections import deque

def bfs_all_paths_costs(graph, start, goal):
    queue = deque()
    queue.append((start, [start], 0))   # (node, path, cost)
    results = []
    price=0

    while queue:
        current, path, cost = queue.popleft()

        if current == goal:
            results.append((path, cost))
            # don't break — we want *all* paths
        
        # expand neighbors breadth-first
        for neighbor, step_cost in graph[current].items():
            
            if neighbor not in path:  # avoid cycles
                price=price+ step_cost 
                queue.append(( neighbor, path + [neighbor],price ))

    return results



# Define the graph
graph = {
    "Chicago": {"Detroit": 283, "Cleveland": 345, "Indianapolis": 182},
    "Detroit": {"Chicago": 283, "Cleveland": 169, "Buffalo": 256},
    "Cleveland": {"Detroit": 169, "Pittsburgh": 134, "Columbus": 144, "Chicago": 345, "Buffalo": 189},
    "Columbus": {"Cleveland": 144, "Indianapolis": 176, "Pittsburgh": 185},
    "Indianapolis": {"Chicago": 182, "Columbus": 176},
    "Pittsburgh": {"Cleveland": 134, "Buffalo": 215, "Philadelphia": 305, "Columbus": 185, "Baltimore": 247},
    "Buffalo": {"Detroit": 256, "Pittsburgh": 215, "Syracuse": 150, "Cleveland": 189},
    "Syracuse": {"Buffalo": 150, "New York": 254, "Boston": 312, "Philadelphia": 253},
    "New York": {"Syracuse": 254, "Philadelphia": 97, "Boston": 215, "Providence": 181},
    "Philadelphia": {"New York": 97, "Pittsburgh": 305, "Baltimore": 101, "Syracuse": 253},
    "Baltimore": {"Philadelphia": 101,"Pittsburgh":247},
    "Boston": {"Syracuse": 312, "Providence": 50, "New York": 215, "Portland": 107},
    "Providence": {"Boston": 50, "New York": 181},
    "Portland": {"Boston": 107}
}

bfs_results = bfs_all_paths_costs(graph, "Syracuse", "Chicago")
count=0
print("\nBFS Paths & Costs:")
for path, cost in bfs_results:
    print(path, "=>", cost)
    count=count+1
print(count)