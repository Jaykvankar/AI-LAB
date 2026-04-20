# Resolution Method with detailed tracing

def resolve(ci, cj):
    resolvents = []
    for di in ci:
        for dj in cj:
            # Check complementary literals
            if di == ('¬' + dj) or ('¬' + di) == dj:
                new_clause = (ci | cj) - {di, dj}
                resolvents.append(new_clause)
    return resolvents


def resolution(kb, query):
    clauses = [set(c) for c in kb]

    # Step 1: Add negated query
    neg_query = '¬' + query
    clauses.append({neg_query})

    print("\nInitial Clauses:")
    for c in clauses:
        print(c)

    step = 1

    while True:
        new = []

        print("\n--- Resolution Step", step, "---")

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                ci, cj = clauses[i], clauses[j]
                resolvents = resolve(ci, cj)

                for r in resolvents:
                    print(f"Resolving {ci} and {cj} → {r}")

                    # Empty clause → contradiction
                    if not r:
                        print("\n Empty clause found (contradiction)")
                        print(" Query is TRUE")
                        return True

                    if r not in clauses and r not in new:
                        new.append(r)

        # No new clauses
        if not new:
            print("\nNo new clauses generated")
            print(" Query is FALSE (cannot be proved)")
            return False

        # Add new clauses
        for r in new:
            print("Adding new clause:", r)
            clauses.append(r)

        step += 1


kb1 = [
    ['P', 'Q'],
    ['¬P', 'R'],
    ['¬Q', 'S'],
    ['¬R', 'S']
]

query1 = 'S'

print("\n========== EXAMPLE 1 ==========")
result1 = resolution(kb1, query1)
print("Result:", result1)

kb2 = [
    ['P', 'Q'],
    ['Q', 'R'],
    ['S', '¬R'],
    ['P']
]

query2 = 'S'

print("\n========== EXAMPLE 2 ==========")
result2 = resolution(kb2, query2)
print("Result:", result2)