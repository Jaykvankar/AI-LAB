class Problem:
    def __init__(self):
        self.INITIAL = (3, 3, 1) 

    def IS_GOAL(self, state):
        return state == (0, 0, 0)

    def ACTIONS(self, state):
        return [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    def RESULT(self, state, action):
        g, b, boat = state
        dg, db = action
        if boat == 1: 
            return (g - dg, b - db, 0)
        else: 
            return (g + dg, b + db, 1)

    def IS_VALID(self, state):
        g, b, boat = state
        if not (0 <= g <= 3 and 0 <= b <= 3): return False
        if g > 0 and g < b: return False
        rg, rb = 3 - g, 3 - b
        if rg > 0 and rg < rb: return False
        return True

class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.STATE = state
        self.PARENT = parent
        self.ACTION = action
        self.DEPTH = depth

def IS_CYCLE(node):
    curr = node.PARENT
    while curr:
        if curr.STATE == node.STATE: return True
        curr = curr.PARENT
    return False

def EXPAND(problem, node):
    for action in problem.ACTIONS(node.STATE):
        next_state = problem.RESULT(node.STATE, action)
        if problem.IS_VALID(next_state):
            yield Node(state=next_state, parent=node, action=action, depth=node.DEPTH + 1)

def DEPTH_LIMITED_SEARCH(problem, l):
    frontier = [Node(problem.INITIAL)] 
    result = "failure"
    explored_count = 0  # Counter for states explored
    
    while frontier:
        node = frontier.pop()
        explored_count += 1
        
        if problem.IS_GOAL(node.STATE): 
            return node, explored_count
        
        if node.DEPTH > l:
            result = "cutoff"
        elif not IS_CYCLE(node):
            for child in EXPAND(problem, node):
                frontier.append(child)
                
    return result, explored_count

# Execution
river_problem = Problem()
print("--- RUNNING DEPTH LIMITED SEARCH (LIMIT=3) ---")
result, count = DEPTH_LIMITED_SEARCH(river_problem, 3)
print(f"Result: {result if isinstance(result, str) else result.STATE}")
print(f"States Explored: {count}")