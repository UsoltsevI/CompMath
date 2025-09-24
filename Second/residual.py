from matrix import Matrix

def residual(a: Matrix, b: Matrix, xk: Matrix) -> Matrix:
    """
    Вычислить невязку по формуле a * xk - b
    """
    return a * xk - b