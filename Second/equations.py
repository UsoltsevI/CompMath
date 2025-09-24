from matrix import Matrix

def get_matrix_y() -> tuple[Matrix, Matrix]:
    """Уравение для варианта (у)"""
    n = 12
    a = Matrix(n, n)
    b = Matrix(n, 1)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i == j):
                a[i - 1, i - 1] = 1.0
            else:
                a[i - 1, j - 1] = 1 / (i ** 2.0 + j)
        
        b[i - 1, 0] = 1 / i

    return a, b
