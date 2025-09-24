from matrix import Matrix

def solve_jakobi(a: Matrix, b: Matrix, x0: Matrix, k: int) -> Matrix:
    """
    Решить уравнение методом Якоби ax = b

    Args:
        k: количество итераций
    """
    l = a.get_l()
    u = a.get_u()
    d = a.diag()
    d1 = d.inverse()

    # x_k+1 = v * x_k + g
    v: Matrix = (d1 * (-1)) * (l + u)
    g: Matrix = d1 * b

    x_k: Matrix = x0.copy()

    for i in range(k):
        x_k = v * x_k + g

    return x_k

