from matrix import Matrix
from matrix_special import get_inversed_diag, inverse_lower_triangular

def solve_seidel(a: Matrix, b: Matrix, x0: Matrix, k: int) -> Matrix:
    """
    Решение СЛАУ методом Зейделя

    Args:
        k: количество итераций
    """

    l = a.get_l()
    u = a.get_u()
    d = a.diag()
    d1 = get_inversed_diag(d)

    ld1 = inverse_lower_triangular(l + d)
    # x_k+1 = v * x_k + g
    v: Matrix = ld1 * u * (-1)
    # g: Matrix = (l + d).inverse() * b
    g: Matrix = ld1 * b

    x_k = x0.copy()

    for i in range(k):
        x_k = (v * x_k) + g

    return x_k

