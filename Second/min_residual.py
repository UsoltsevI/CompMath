from matrix import Matrix
from residual import residual
from scalar import mul_scalar

def solve_min_residual(a: Matrix, b: Matrix, x0: Matrix, k: int) -> Matrix:
    """
    Решить систему методом минимальных невязок
    """

    # TODO: проверить условия
    xk = x0.copy()

    for i in range(k):
        rk = residual(a, b, xk) # невязка
        a_rk = a * rk 
        tau = mul_scalar(a_rk, rk) / mul_scalar(a_rk, a_rk) # оптимальный tau
        xk = xk - rk * tau

    return xk