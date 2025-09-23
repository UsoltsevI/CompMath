import matrix

#
# Решение СЛАУ методом Зейделя
#
# k - количество итераций
#
def solve_seidel(a: list[list[float]], b: list[float], x0: list[float], k: int) -> list[float]:
    assert(len(a) > 0)
    assert(len(a) == len(b) and len(a[0]) == len(b))

    l = matrix.get_l(a)
    u = matrix.get_u(a)
    d = matrix.diag(a)
    d1 = matrix.diag_d1(d)

    # x_k+1 = v * x_k + g
    v: list[list[float]] = matrix.multiply_k(matrix.multiply(matrix.sum(l, d1), u), -1)
    g: list[list[float]] = matrix.multiply(matrix.inverse(matrix.sum(l, d)), matrix.column_to_matrix(b))

    x_k = matrix.column_to_matrix(x0.copy())

    for i in range(k):
        x_k = matrix.sum(matrix.multiply(v, x_k), g)

    return matrix.matrix_to_line(x_k)

