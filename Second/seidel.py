from matrix import Matrix

#
# Решение СЛАУ методом Зейделя
#
# k - количество итераций
#
def solve_seidel(a: Matrix, b: Matrix, x0: Matrix, k: int) -> Matrix:
    l = a.get_l()
    u = a.get_u()
    d = a.diag()
    d1 = d.inverse()

    # x_k+1 = v * x_k + g
    v: Matrix = (l + d1) * u * (-1)
    g: Matrix = (l + d).inverse() * b

    x_k = x0.copy()

    for i in range(k):
        x_k = (v * x_k) + g

    return x_k

