graph = {
    "Chicago": {"Detroit": 283, "Cleveland": 345, "Indianapolis": 182},
    "Detroit": {"Chicago": 283, "Cleveland": 169, "Buffalo": 256},
    "Cleveland": {"Detroit": 169, "Pittsburgh": 134, "Columbus": 144, "Chicago": 345},
    "Columbus": {"Cleveland": 144, "Indianapolis": 176, "Pittsburgh": 185},
    "Indianapolis": {"Chicago": 182, "Columbus": 176},
    "Pittsburgh": {"Cleveland": 134, "Buffalo": 215, "Philadelphia": 305, "Columbus": 185},
    "Buffalo": {"Detroit": 256, "Pittsburgh": 215, "Syracuse": 150},
    "Syracuse": {"Buffalo": 150, "New York": 254, "Boston": 312},
    "New York": {"Syracuse": 254, "Philadelphia": 97, "Boston": 215},
    "Philadelphia": {"New York": 97, "Pittsburgh": 305, "Baltimore": 101},
    "Baltimore": {"Philadelphia": 101},
    "Boston": {"Syracuse": 312, "Providence": 50, "New York": 215, "Portland": 107},
    "Providence": {"Boston": 50},
    "Portland": {"Boston": 107}
}

start = "Syracuse"
target = "Chicago"

#DFS
def stuck(x, seen): #Check if from city x, there is still a path to the target
    if x == target:
        return False
    for y in graph[x]:
        if y not in seen:
            seen.add(y)
            if not stuck(y, seen):
                return False
    return True

def search(path): #search for the path
    x = path[-1] 
    if x == target:
        dis = 0
        for i in range(len(path) - 1):
            dis += graph[path[i]][path[i+1]]
        print(" -> ".join(path), f" Total Distance: {dis} miles")
        return
    
    seen = set(path)
    if stuck(x, set(seen)):
        return
    
    for y in graph[x]:
        if y not in path:
            path.append(y)
            search(path)
            path.pop()

print(f"All possible paths from {start} to {target}:\n")
search([start])



