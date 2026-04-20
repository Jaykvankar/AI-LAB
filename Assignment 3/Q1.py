import random

states = {
    ("A","dirty") : "suck",
    ("A","clean") : "MoveRight",
    ("B","dirty") : "suck",
    ("B","clean") : random.choice(["MoveLeft","MoveRight"]),
    ("C","dirty") : "suck",
    ("C","clean") : "MoveLeft"
}

condition = {
    "A" : "dirty",
    "B" : "dirty",
    "C" : "dirty"
}

present_location = "A"
step = 1
total_cost = 0

# Run until all rooms are clean
while "dirty" in condition.values():
    percept = (present_location, condition[present_location])
    action = states[percept]
    print(f"Step {step}: Location={present_location}, Status={condition[present_location]}, Action={action}")

    if action == "suck":
        condition[present_location] = "clean"
        total_cost += 2   
    elif action == "MoveRight":
        if present_location == "A":
            present_location = "B"
        else:
            present_location = "C"
        total_cost += 1 
    elif action == "MoveLeft":
        if present_location == "C":
            present_location = "B"
        else:
            present_location = "A"
        total_cost += 1  

    step += 1

print("\nAll rooms are clean!")
print("Final room status:", condition)
print("Total cost incurred:", total_cost)