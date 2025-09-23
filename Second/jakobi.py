import matrix

#
# Решить уравнение методом Якоби ax = b
#
# k - количество итераций
#
def solve_jakobi(a: list[list[float]], b: list[float], x0: list[float], k: int) -> list[float]:
    assert(len(a) > 0)
    assert(len(a) == len(b) and len(a[0]) == len(b))

    l = matrix.get_l(a)
    u = matrix.get_u(a)
    d = matrix.diag(a)
    d1 = matrix.diag_d1(d)

    # x_k+1 = v * x_k + g
    v: list[list[float]] = matrix.multiply(matrix.multiply_k(d1, -1), matrix.sum(l, u))
    g: list[list[float]] = matrix.multiply(d1, matrix.column_to_matrix(b))

    x_k = matrix.column_to_matrix(x0.copy())

    for i in range(k):
        x_k = matrix.sum(matrix.multiply(v, x_k), g)

    return matrix.matrix_to_line(x_k)

