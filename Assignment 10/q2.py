"""
Q2: Erratic Vacuum Agent — AND-OR Graph Search

State: (location, A_state, B_state)
Location: 0=A, 1=B
State: 0=Clean, 1=Dirty

Erratic behaviors:
  CLEAN on dirty  → cleans current, SOMETIMES also cleans adjacent  (lucky)
  CLEAN on clean  → stays clean OR deposits dirt on current         (unlucky)

AND-OR Search:
  OR  node → agent picks an action (agent's choice)
  AND node → ALL outcomes must lead to goal (environment's choice)
"""

from itertools import product

def is_goal(state):
    _, sA, sB = state
    return sA == 0 and sB == 0

def successors(state, action):
    loc, sA, sB = state
    other = 1 - loc

    if action == 'Move':
        return [((other, sA, sB), 'Moves to ' + ('B' if loc == 0 else 'A'))]

    # Clean action — nondeterministic
    cur_dirty = sA if loc == 0 else sB
    outcomes = []

    if cur_dirty == 1:  # current tile is DIRTY
        # Outcome 1: cleans current only
        nA = 0 if loc == 0 else sA
        nB = 0 if loc == 1 else sB
        outcomes.append(((loc, nA, nB), 'Cleans current tile only'))
        # Outcome 2: cleans current AND adjacent (lucky!)
        if (loc, 0, 0) != (loc, nA, nB):  # only add if different
            outcomes.append(((loc, 0, 0), 'Cleans current AND adjacent tile (lucky!)'))
    else:  # current tile is CLEAN
        # Outcome 1: nothing happens, stays clean
        outcomes.append(((loc, sA, sB), 'No effect, tile stays clean'))
        # Outcome 2: deposits dirt (unlucky!)
        nA = 1 if loc == 0 else sA
        nB = 1 if loc == 1 else sB
        if (loc, nA, nB) != (loc, sA, sB):
            outcomes.append(((loc, nA, nB), 'Deposits dirt on current tile (unlucky!)'))

    # deduplicate by state
    seen = set()
    unique = []
    for (s, desc) in outcomes:
        if s not in seen:
            seen.add(s)
            unique.append((s, desc))
    return unique

def and_or_search(initial):
    def or_search(state, visited):
        if is_goal(state):
            return 'GOAL'
        if state in visited:
            return None
        visited = visited | {state}
        for action in ['Clean', 'Move']:
            outcome_list = successors(state, action)
            plan = and_search(outcome_list, action, visited)
            if plan is not None:
                return (action, plan)
        return None

    def and_search(outcome_list, action, visited):
        result = {}
        for (s, desc) in outcome_list:
            subplan = or_search(s, visited)
            if subplan is None:
                return None
            result[(s, desc)] = subplan
        return result

    return or_search(initial, frozenset())

def fmt(state):
    loc = 'A' if state[0] == 0 else 'B'
    sA  = 'Dirty' if state[1] == 1 else 'Clean'
    sB  = 'Dirty' if state[2] == 1 else 'Clean'
    return f"[Loc={loc}  A={sA}  B={sB}]"

def print_plan(plan, state, indent=0):
    pad  = '  ' * indent
    pad2 = '  ' * (indent + 1)

    if plan == 'GOAL':
        print(f"{pad}{'─'*55}")
        print(f"{pad}  ✅ GOAL REACHED — Both tiles are Clean!")
        print(f"{pad}{'─'*55}")
        return
    if plan is None:
        print(f"{pad}❌ No plan found")
        return

    action, branches = plan
    print(f"{pad}State : {fmt(state)}")
    print(f"{pad}Action: ▶ {action}")
    print(f"{pad}Environment responds with one of {len(branches)} outcome(s):")

    for i, ((outcome_state, desc), subplan) in enumerate(branches.items(), 1):
        connector = '├──' if i < len(branches) else '└──'
        print(f"{pad2}{connector} Outcome {i}: {desc}")
        print(f"{pad2}    New state: {fmt(outcome_state)}")
        if subplan == 'GOAL':
            print(f"{pad2}    ✅ GOAL REACHED — Both tiles are Clean!")
        else:
            print()
            print_plan(subplan, outcome_state, indent + 3)
    print()

# ─── Run for all 8 states ──────────────────────────────────────────────────
print("=" * 65)
print("   AND-OR GRAPH SEARCH — Erratic Vacuum Agent")
print("=" * 65)
print("  CLEAN on dirty tile → cleans it | sometimes also cleans adjacent")
print("  CLEAN on clean tile → no effect | sometimes deposits dirt")
print("  MOVE               → always deterministic")
print("=" * 65)

# Showing 2 most interesting states
all_states = [
    (0, 1, 1),  # Loc=A, A=Dirty, B=Dirty  (hardest case)
    (1, 1, 0),  # Loc=B, A=Dirty, B=Clean
]
for state in all_states:
    print(f"\n{'━'*65}")
    print(f"  INITIAL STATE: {fmt(state)}")
    print(f"{'━'*65}")
    plan = and_or_search(state)
    if plan == 'GOAL':
        print("  ✅ Already at GOAL — Both tiles Clean!")
    elif plan is None:
        print("  ❌ No plan exists for this state")
    else:
        print()
        print_plan(plan, state, indent=1)