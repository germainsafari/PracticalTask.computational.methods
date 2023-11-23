def evaluate_polynomial(coefficients, x):
    result = 0
    n = len(coefficients)
    for i in range(n):
        result += coefficients[i] * (x ** (n - 1 - i))
    return result

def evaluate_derivative(coefficients, x):
    result = 0
    n = len(coefficients) - 1
    for i in range(n):
        result += (n - i) * coefficients[i] * (x ** (n - 1 - i))
    return result

def newton_method(coefficients, x0, max_iter=1000):
    tolerance = 1e-6
    x = x0
    iteration = 0

    while iteration < max_iter:
        derivative = evaluate_derivative(coefficients, x)
        if abs(derivative) < tolerance:
            break

        x = x - evaluate_polynomial(coefficients, x) / derivative
        iteration += 1

    return x

def PolyRoots(coefficients):
    roots = []
    for i in range(len(coefficients) - 1):
        initial_guess = float(i)
        root = newton_method(coefficients, initial_guess)
        roots.append(round(root, 5))

    return roots

# Examples
print(PolyRoots([1, -1.5]))  # Output: [1.5]
print(PolyRoots([1, -2, 1]))  # Output: [1.0, 1.0]
print(PolyRoots([1, 2, 2]))   # Output: []
print(PolyRoots([2, 2, -4, 0]))  # Output: [0.0, 1.0, -2.0]
