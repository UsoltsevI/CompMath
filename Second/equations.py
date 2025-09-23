import numpy as np

#
# Уравение для варианта (у)
#
def get_matrix_y() -> tuple[list[list[float]], list[float]]:
    n = 12
    a: list[list[float]] = [[0.0] * n for _ in range(0, n)]
    b: list[float]       = np.empty(n, dtype=float)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i == j):
                a[i - 1][i - 1] = 1.0
            else:
                a[i - 1][j - 1] = 1 / (i ** 2.0 + j)
        
        b[i - 1] = 1 / i

    return a, b
