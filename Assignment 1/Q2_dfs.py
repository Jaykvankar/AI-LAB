graph = {
    "Raj": ["Sunil", "Neha_1"],
    "Sunil": ["Raj", "Akash", "Sneha", "Maya"],
    "Akash": ["Sunil", "Priya"],
    "Priya": ["Raj", "Aarav", "Akash"],
    "Neha_1": ["Raj", "Akash", "Sneha", "Aarav"],
    "Sneha": ["Sunil", "Neha_1", "Rahul"],
    "Maya": ["Rahul", "Arjun_1", "Sunil"],
    "Aarav": ["Neha_1", "Arjun_2"],
    "Neha_2": ["Priya", "Neha_1", "Rahul", "Arjun_2"],
    "Rahul": ["Neha_1", "Neha_2", "Sneha", "Maya", "Pooja", "Arjun_2"],
    "Arjun_1": ["Maya", "Pooja"],
    "Arjun_2": ["Aarav", "Neha_2", "Rahul"],
    "Pooja": ["Arjun_1", "Arjun_2", "Rahul"]
}


def print_tree(parent, node, level=0):
    print("  " * level + node)
    for child in parent:
        if parent[child] == node:
            print_tree(parent, child, level + 1)

#DFS
def dfs_tree(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            parent[neighbor] = node
            dfs_tree(graph, neighbor, visited, parent)
    return parent

visited = set()
parent = {"Raj": None}

dfs_tree(graph, "Raj", visited, parent)

print("DFS Tree:")
print_tree(parent, "Raj")