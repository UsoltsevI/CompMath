from matrix import Matrix
from matrix_special import get_inversed_diag, inverse_lower_triangular
from eigenvalues import power_iteration
import math 

def solve_upper_relaxation(A: Matrix, b: Matrix, x0: Matrix, k) -> Matrix:
    """Решить СЛАУ методом верхней релаксации"""

    L = A.get_l()
    U = A.get_u()
    D = A.diag()

    T = Matrix.identity(A.rows) - D * A

    p = power_iteration(T, x0, k)

    if (math.fabs(p) > 1):
        raise ValueError("СЛАУ не подходит для метода верхней релаксации")

    w = 1 + (p / (1 + math.sqrt(1 - p ** 2))) ** 2

    # (wL + D)^{-1}
    wLD1 = inverse_lower_triangular(L * w + D)

    x_k = x0

    # x_{k + 1} = B x_k + g
    g = wLD1 * b * w
    B = wLD1 * (U * w + D * (w - 1)) * (-1) 

    for i in range(k):
        x_k = B * x_k + g

    return x_k
