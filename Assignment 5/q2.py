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

# (Uses the same Problem, Node, IS_CYCLE, and EXPAND from Script 1)

def ITERATIVE_DEEPENING_SEARCH(problem):
    total_states_explored = 0
    for depth in range(20): 
        print(f"Searching depth limit: {depth}")
        result, count = DEPTH_LIMITED_SEARCH(problem, depth)
        total_states_explored += count
        
        if result != "cutoff" and result != "failure":
            return result, total_states_explored
    return "failure", total_states_explored

def print_path(node):
    path = []
    curr = node
    while curr:
        path.append(curr)
        curr = curr.PARENT
    print("\n--- Optimal Solution Path ---")
    for step in reversed(path):
        print(f"Depth {step.DEPTH}: {step.STATE} (Action: {step.ACTION})")

# Execution
river_problem = Problem()
print("--- RUNNING ITERATIVE DEEPENING SEARCH ---")
ids_result, total_count = ITERATIVE_DEEPENING_SEARCH(river_problem)

if isinstance(ids_result, Node):
    print_path(ids_result)
    print(f"\nTotal States Explored across all iterations: {total_count}")
else:
    print(f"Result: {ids_result}")