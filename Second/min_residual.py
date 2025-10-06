from matrix import Matrix
from residual import residual
from scalar import mul_scalar
from eigenvalues import norm_l2

def solve_min_residual(a: Matrix, b: Matrix, x0: Matrix, k: int) -> tuple[Matrix, list[float]]:
    """
    Решить систему методом минимальных невязок
    """

    # TODO: проверить условия
    xk = x0.copy()

    rk_arr = [0.0] * k

    for i in range(k):
        rk = residual(a, b, xk) # невязка
        a_rk = a * rk 
        tau = mul_scalar(a_rk, rk) / mul_scalar(a_rk, a_rk) # оптимальный tau
        xk = xk - rk * tau
        rk_arr[i] = norm_l2(residual(a, b, xk))

    return xk, rk_arr