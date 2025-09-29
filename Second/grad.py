from matrix import Matrix
from residual import residual
from scalar import mul_scalar

def solve_grad(a: Matrix, b: Matrix, x0: Matrix, k: int) -> Matrix:
    """
    Решить систему методом градиентного спуска
    """

    xk = x0.copy()

    for i in range(k):
        rk = residual(a, b, xk) # невязка
        tau = mul_scalar(rk, rk) / mul_scalar(a * rk, rk) # оптимальный tau
        xk = xk - rk * tau

    return xk
