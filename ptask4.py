def gauss_elimination(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(min(rows, cols - 1)):
        # Partial pivoting to avoid division by zero
        max_row = max(range(i, rows), key=lambda x: abs(matrix[x][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Make the diagonal element 1
        pivot = matrix[i][i]
        if pivot != 0:
            matrix[i] = [elem / pivot for elem in matrix[i]]

        # Eliminate other rows
        for j in range(rows):
            if i != j:
                factor = matrix[j][i]
                matrix[j] = [elem_j - factor * elem_i for elem_i, elem_j in zip(matrix[i], matrix[j])]

    return matrix

def find_solutions(matrix):
    rows, cols = len(matrix), len(matrix[0]) - 1
    solutions = []

    for row in matrix:
        if all(elem == 0 for elem in row[:-1]):
            # Check if the row is all zeros except the last element
            if row[-1] != 0:
                return []  # Inconsistent system
        else:
            solutions.append(row[-1])

    # Check if there are more variables than equations (underdetermined system)
    if rows < cols:
        return []

    return solutions

def SystemSolve(matrix):
    # Apply Gaussian elimination to the augmented matrix
    reduced_matrix = gauss_elimination(matrix)

    # Find solutions from the reduced echelon form
    solutions = find_solutions(reduced_matrix)

    return solutions

# Examples
print(SystemSolve([[0, 4, 2, -2], [-2, 3, 1, -7], [4, 5, 2, 4]]))
# Output: [2.0, -2.0, 3.0]

print(SystemSolve([[1, 3, 5], [2, 6, 5]]))
# Output: []

print(SystemSolve([[1, 3, 5], [3, -2, 4], [4, -1, 9], [7, -3, 13]]))
# Output: [2.0, 1.0]
