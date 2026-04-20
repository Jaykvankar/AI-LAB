class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Path cost
        self.h = h  # Heuristic
        self.f = g + h  # Total cost

def get_h(p1, p2):
    # Manhattan distance for grid movement
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Maze structure from image
maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 0, 0, 3],
    [0, 3, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [3, 0, 0, 0, 3]
]

def a_star(start, goal):
    frontier = [Node(start, None, 0, get_h(start, goal))]
    reached = {}

    while frontier:
        # Pick node with lowest f cost
        m_idx = 0
        for i in range(1, len(frontier)):
            if frontier[i].f < frontier[m_idx].f:
                m_idx = i
        
        curr = frontier.pop(m_idx)
        if curr.state == goal:
            return curr

        reached[curr.state] = curr.g
        
        r, c = curr.state
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and maze[nr][nc] != 1:
                st = (nr, nc)
                new_g = curr.g + 1
                if st not in reached or new_g < reached[st]:
                    print(f"Expanding node {st} with g={new_g}, h={get_h(st, goal)}, f={new_g + get_h(st, goal)}")
                    frontier.append(Node(st, curr, new_g, get_h(st, goal)))
    return None

def solve():
    curr_pos = (0, 0)
    rewards = [(2, 1), (4, 0), (1, 4), (4, 4)]
    total_path = [curr_pos]
    total_cost = 0

    while rewards:
        # Target nearest reward
        target = rewards[0]
        min_d = get_h(curr_pos, target)
        for r in rewards:
            if get_h(curr_pos, r) < min_d:
                min_d = get_h(curr_pos, r)
                target = r

        res = a_star(curr_pos, target)
        if res:
            # Reconstruct path segment
            segment = []
            temp = res
            while temp.parent:
                segment.append(temp.state)
                temp = temp.parent
            segment.reverse()
            
            total_path.extend(segment)
            total_cost += res.g
            curr_pos = target
            rewards.remove(target)

    print("Path Taken:", total_path)
    print("Total Path Cost:", total_cost)

solve()