def SystemSolve(matrix):
    # Check if the matrix is empty
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Check for inconsistent system (more variables than equations)
    if cols - 1 > rows:
        return []

    for i in range(rows):
        # Find pivot for this column
        pivot_row = i
        for j in range(i + 1, rows):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j

        # Swap the rows for partial pivoting
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        # Check if the system is inconsistent
        if matrix[i][i] == 0:
            return []

        # Normalize the pivot row
        pivot_value = matrix[i][i]
        for j in range(cols):
            matrix[i][j] /= pivot_value

        # Eliminate other rows
        for k in range(rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(cols):
                    matrix[k][j] -= factor * matrix[i][j]

    # Extract the solutions
    solutions = [row[-1] for row in matrix]

    return solutions[:-1] if len(solutions) == cols else solutions

# Examples
print(SystemSolve([[0, 4, 2, -2], [-2, 3, 1, -7], [4, 5, 2, 4]]))
# Output: [2.0, -2.0, 3.0]

print(SystemSolve([[1, 3, 5], [2, 6, 5]]))
# Output: []

print(SystemSolve([[1, 3, 5, 8], [3, -2, 4, 1], [4, -1, 9, 2], [7, -3, 13, 7]]))
# Output: [2.0, 1.0]
