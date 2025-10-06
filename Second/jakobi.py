from matrix_special import get_inversed_diag
from matrix import Matrix
from eigenvalues import norm_l2
from residual import residual

def solve_jakobi(a: Matrix, b: Matrix, x0: Matrix, k: int) -> tuple[Matrix, list[float]]:
    """
    Решить уравнение методом Якоби ax = b

    Args:
        k: количество итераций
    """
    l = a.get_l()
    u = a.get_u()
    d = a.diag()

    # Создаём матрицу, обратную диагональной
    d1 = get_inversed_diag(d)

    rk_arr = [0.0] * k;

    # x_k+1 = v * x_k + g
    v: Matrix = (d1 * (-1)) * (l + u)
    g: Matrix = d1 * b

    x_k: Matrix = x0.copy()

    for i in range(k):
        x_k = v * x_k + g
        rk_arr[i] = norm_l2(residual(a, b, x_k))

    return x_k, rk_arr
