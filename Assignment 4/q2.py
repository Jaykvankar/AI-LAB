class Node:
    def __init__(self, x, y, cost, path):
        self.x = x
        self.y = y
        self.cost = cost
        self.path = path


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def push(self, node):
        self.pq.append(node)

    def pop(self):
        min_index = 0
        for i in range(1, len(self.pq)):
            if self.pq[i].cost < self.pq[min_index].cost:
                min_index = i
        best = self.pq[min_index]
        self.pq.pop(min_index)
        return best

    def empty(self):
        return len(self.pq) == 0


# Floor Map
floor = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1],
[1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1],
[1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1],
[1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1],
[1,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1],
[1,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1],
[1,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Printable Map
sol = [
list("#### ####################"),
list("#     ##  ##  ##  #######"),
list("#     ##  ##  ##  #######"),
list("#     ##  ##  ##  #######"),
list("##   #### ## # ## #######"),
list("#                     E #"),
list("##   #### # ## ##       #"),
list("##   #   # ## ##        #"),
list("##   # # # ## ##        #"),
list("##S  # # # ## ##        #"),
list("#### ####################")
]

rows = len(floor)
cols = len(floor[0])

sx, sy = 9, 3
gx, gy = 5, 21

visited = [[False for _ in range(cols)] for _ in range(rows)]

pq = PriorityQueue()

start = Node(sx, sy, 0, [(sx, sy)])
pq.push(start)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

explored = 0

print("\nBest First Search (Cost Only)\n")

while not pq.empty():
    curr = pq.pop()
    explored += 1

    x = curr.x
    y = curr.y

    if visited[x][y]:
        continue

    visited[x][y] = True
    sol[x][y]="*"
    
    if x == gx and y == gy:
        print("Evacuation Path:")
        for (px, py) in curr.path:
            print(f"({px},{py})", end="")
            sol[px][py] = '.'

        print("\n")
        for i in range(len(sol)):
            for j in range(len(sol[i])):
                print(sol[i][j], end="")
            print()


        print("\nCells explored:", explored)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < rows and 0 <= ny < cols:
            if not visited[nx][ny] and floor[nx][ny] == 0:
                new_path = curr.path.copy()
                new_path.append((nx, ny))
                next_node = Node(nx, ny, curr.cost + 1, new_path)
                pq.push(next_node)
