# Generate all possible next states
def generate_states(state):
    states = []
    zero_pos = state.index(0)

    # Move UP
    if zero_pos not in [0, 1, 2]:
        new_state = state[:]
        new_state[zero_pos], new_state[zero_pos - 3] = \
            new_state[zero_pos - 3], new_state[zero_pos]
        states.append(new_state)

    # Move LEFT
    if zero_pos not in [0, 3, 6]:
        new_state = state[:]
        new_state[zero_pos], new_state[zero_pos - 1] = \
            new_state[zero_pos - 1], new_state[zero_pos]
        states.append(new_state)

    # Move DOWN
    if zero_pos not in [6, 7, 8]:
        new_state = state[:]
        new_state[zero_pos], new_state[zero_pos + 3] = \
            new_state[zero_pos + 3], new_state[zero_pos]
        states.append(new_state)

    # Move RIGHT
    if zero_pos not in [2, 5, 8]:
        new_state = state[:]
        new_state[zero_pos], new_state[zero_pos + 1] = \
            new_state[zero_pos + 1], new_state[zero_pos]
        states.append(new_state)

    return states

# DFS
def dfs(initial_state, goal_state):
    stack = [initial_state]
    visited = set([tuple(initial_state)])
    states_explored = 0

    while stack:
        current_state = stack.pop()

        if current_state == goal_state:
            print("DFS Goal Found")
            print("DFS States Explored:", states_explored)
            return
        states_explored += 1

        for next_state in generate_states(current_state):
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                stack.append(next_state)

    print("Goal not found using DFS")


#MAIN
initial_state = [7, 2, 4,
                 5, 0, 6,
                 8, 3, 1]

goal_state = [0, 1, 2,
              3, 4, 5,
              6, 7, 8]

dfs(initial_state, goal_state)