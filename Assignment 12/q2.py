grid = [
    [0,0,0,0,0,6,0,0,0],
    [0,5,9,0,0,0,0,0,8],
    [2,0,0,0,0,8,0,0,0],
    [0,4,5,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,0,0],
    [0,0,6,0,0,3,0,5,0],
    [0,0,0,0,0,7,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,5,0,0,0,2]
]

#all 81 cells
variables = [(r,c) for r in range(9) for c in range(9)]

#domain: fixed=given digit, empty={1..9}
domains = {}
for r in range(9):
    for c in range(9):
        domains[(r,c)] = {grid[r][c]} if grid[r][c] != 0 else set(range(1,10))

#neighbors same row, col, or box
def get_neighbors(r,c):
    seen = set()
    for i in range(9):
        if i != c: seen.add((r,i))
        if i != r: seen.add((i,c))
    br, bc = 3*(r//3), 3*(c//3)
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if (i,j) != (r,c): seen.add((i,j))
    return seen

neighbors = {v: get_neighbors(*v) for v in variables}

#remove values from xi that have no support in xj
def revise(xi, xj):
    bad = {x for x in domains[xi] if all(x == y for y in domains[xj])}
    domains[xi] -= bad
    return len(bad)

#ac-3 main loop
def ac3():
    queue = [(xi, xj) for xi in variables for xj in neighbors[xi]]
    total_arcs = len(queue)
    removed = 0
    while queue:
        xi, xj = queue.pop(0)
        n = revise(xi, xj)
        if n:
            removed += n
            if not domains[xi]:
                return False, removed, total_arcs
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True, removed, total_arcs

#backup domains
saved = {v: set(domains[v]) for v in variables}
result, removed, total_arcs = ac3()

print("= ac-3 result =")
print("arcs generated:", total_arcs)
print("values removed:", removed)

print("\ndomain sizes:")
for r in range(9):
    print(" ".join(str(len(domains[(r,c)])) for c in range(9)))

solved = all(len(domains[v]) == 1 for v in variables)
broken = any(len(domains[v]) == 0 for v in variables)

print("\nsolved:", solved)
print("contradiction:", broken)
if solved:
    print("puzzle fully solved by ac-3")
elif broken:
    print("no solution exists")
else:
    print("partially pruned, backtracking needed")