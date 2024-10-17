from itertools import permutations

def total_cost(assignment, cost_matrix):
    return sum(cost_matrix[i][task] for i, task in enumerate(assignment))

def assignment_problem(cost_matrix):
    min_cost, best_assignment = float('inf'), None
    for perm in permutations(range(len(cost_matrix))):
        cost = total_cost(perm, cost_matrix)
        if cost < min_cost:
            min_cost, best_assignment = cost, perm
    return min_cost, best_assignment

def test_assignment_problem():
    test_cases = [
        [[3, 10, 7], [8, 5, 12], [4, 6, 9]],
        [[15, 9, 4], [8, 7, 18], [6, 12, 11]]
    ]

    for i, matrix in enumerate(test_cases, 1):
        min_cost, assignment = assignment_problem(matrix)
        print(f"Test Case {i}:")
        print(f"Optimal Assignment: {[(f'worker {i+1}', f'task {t+1}') for i, t in enumerate(assignment)]}")
        print(f"Total Cost: {min_cost}\n")

if __name__ == "__main__":
    test_assignment_problem()
