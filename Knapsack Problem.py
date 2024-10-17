from itertools import combinations

def total_value(items, values):
    return sum(values[i] for i in items)

def is_feasible(items, weights, capacity):
    return sum(weights[i] for i in items) <= capacity

def knapsack_01(weights, values, capacity):
    n = len(weights)
    best_value, best_selection = 0, []
    for r in range(n + 1):
        for items in combinations(range(n), r):
            if is_feasible(items, weights, capacity):
                value = total_value(items, values)
                if value > best_value:
                    best_value, best_selection = value, items

    return best_value, list(best_selection)

weights = [2, 3, 1]
values = [4, 5, 3]
capacity = 4

best_value, best_selection = knapsack_01(weights, values, capacity)
print(f"Optimal Selection: {best_selection}")
print(f"Total Value: {best_value}")
