def dp(problem):
    [capacity, prices, weights] = problem

    # calculate solution matrix
    solution_matrix = [[0 for _ in range(0, capacity + 1)] for _ in range(0, len(prices) + 1)]
    for i in range(1, len(solution_matrix)):
        for j in range(1, len(solution_matrix[i])): 
            only_previous_items = solution_matrix[i - 1][j]
            if j - weights[i - 1] < 0:
                with_current_item = 0
            else:
                with_current_item = solution_matrix[i - 1][j - weights[i - 1]] + prices[i - 1]
            solution_matrix[i][j] = max(only_previous_items, with_current_item)

    # calculate solution
    solution = []
    remaining_capacity = capacity
    for i in range(len(prices), 0, -1):
        if solution_matrix[i][remaining_capacity] == solution_matrix[i - 1][remaining_capacity]:
            solution.append(0)
        else:
            remaining_capacity -= weights[i - 1]
            solution.append(1)
    solution.reverse()
    print(solution)

    return solution_matrix[len(prices)][capacity]

if __name__ == '__main__':
    problem = [165, [92, 57, 49, 68, 60, 43, 67, 84, 87, 72], [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]]
    solution = dp(problem)
    print(solution)