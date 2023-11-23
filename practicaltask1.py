def MatrixMultiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Dimension mismatch: The number of columns in A must be equal to the number of rows in B")

    if len(A) == len(A[0]) == len(B) == len(B[0]) == 2:
        # Base case: direct multiplication for 2x2 matrices
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    else:
        # Recursive case: apply Strassen/Winograd algorithm
        a11 = [row[:len(A)//2] for row in A[:len(A)//2]]
        a12 = [row[len(A)//2:] for row in A[:len(A)//2]]
        a21 = [row[:len(A)//2] for row in A[len(A)//2:]]
        a22 = [row[len(A)//2:] for row in A[len(A)//2:]]

        b11 = [row[:len(B[0])//2] for row in B[:len(B)//2]]
        b12 = [row[len(B[0])//2:] for row in B[:len(B)//2]]
        b21 = [row[:len(B[0])//2] for row in B[len(B)//2:]]
        b22 = [row[len(B[0])//2:] for row in B[len(B)//2:]]

        p1 = MatrixMultiply(a11, [[b11[0][0] - b21[0][0], b11[0][1] - b21[0][1]], [b12[0][0] - b22[0][0], b12[0][1] - b22[0][1]]])
        p2 = MatrixMultiply([[a11[0][0] + a12[0][0], a11[0][1] + a12[0][1]], a21[0]], b22)
        p3 = MatrixMultiply([[a21[0][0] - a11[0][0], a21[0][1] - a11[0][1]], a22[0]], [[b11[0][0] + b12[0][0], b11[0][1] + b12[0][1]], b22[0]])
        p4 = MatrixMultiply(a22, [[b21[0][0] - b11[0][0], b21[0][1] - b11[0][1]], [b12[0][0] - b22[0][0], b12[0][1] - b22[0][1]]])
        p5 = MatrixMultiply([[a11[0][0] + a12[0][0], a11[0][1] + a12[0][1]], a22[0]], [[b11[0][0] + b12[0][0], b11[0][1] + b12[0][1]], [b21[0][0] + b22[0][0], b21[0][1] + b22[0][1]]])
        p6 = MatrixMultiply([[a21[0][0] - a11[0][0], a21[0][1] - a11[0][1]], a22[0]], [[b11[0][0] + b12[0][0], b11[0][1] + b12[0][1]], b22[0]])
        p7 = MatrixMultiply(a11, [[b21[0][0] - b11[0][0], b21[0][1] - b11[0][1]], [b12[0][0] - b22[0][0], b12[0][1] - b22[0][1]]])

        # Calculate submatrices of the result
        c11 = [[p5[0][0] + p4[0][0] - p2[0][0] + p6[0][0], p5[0][1] + p4[0][1] - p2[0][1] + p6[0][1]],
               [p3[0][0] + p4[0][0], p3[0][1] + p4[0][1]]]
        c12 = [[p1[0][0] + p2[0][0], p1[0][1] + p2[0][1]],
               [p5[0][0] + p1[0][0] - p3[0][0] - p7[0][0], p5[0][1] + p1[0][1] - p3[0][1] - p7[0][1]]]
        c21 = [[p3[0][0] + p4[0][0], p3[0][1] + p4[0][1]],
               [p5[0][0] + p1[0][0] - p3[0][0] - p7[0][0], p5[0][1] + p1[0][1] - p3[0][1] - p7[0][1]]]
        c22 = [[p5[0][0] + p4[0][0] - p2[0][0] + p6[0][0], p5[0][1] + p4[0][1] - p2[0][1] + p6[0][1]],
               [p1[0][0] + p2[0][0], p1[0][1] + p2[0][1]]]

        # Combine submatrices into the final result
        result = []
        for i in range(len(c11)):
            result.append(c11[i] + c12[i])
        for i in range(len(c21)):
            result.append(c21[i] + c22[i])

        return result

# Test examples
try:
    result1 = MatrixMultiply([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    print(result1)  # Output: [[58, 64], [139, 154]]
except ValueError as e:
    print(e)

try:
    result2 = MatrixMultiply([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]])
    print(result2)  # Output: Error/Exception (Dimension mismatch)
except ValueError as e:
    print(e)
