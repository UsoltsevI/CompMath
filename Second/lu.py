from matrix import Matrix

def solve_lu(A: Matrix, b: Matrix) -> Matrix:
    """Найти решение методом LU разложения"""

    # Находим LU разложение
    L, U = find_lu(A)

    # Ly = b
    y = Matrix(A.rows, 1)

    for i in range(A.rows):
        sum = 0.0

        for p in range(i):
            sum += y[p, 0] * L[i, p]

        y[i, 0] = (b[i, 0] - sum) / L[i, i]

    # Ux = y
    x = Matrix(A.rows, 1)

    for i in range(A.rows - 1, -1, -1):
        sum = 0.0

        for p in range(A.rows - 1, i, -1):
            sum += x[p, 0] * U[i, p]

        x[i, 0] = (y[i, 0] - sum) / U[i, i] 

    return x


def find_lu(A: Matrix) -> tuple[Matrix, Matrix]:
    """Найти L и U такие, что A = LU"""

    L = Matrix.zeros(A.rows, A.cols)
    U = Matrix.zeros(A.rows, A.cols)

    for i in range(A.rows):
        L[i, i] = 1
    
    for i in range(A.rows):
        for j in range (A.rows):
            if (i <= j):
                sum = 0.0
                for k in range(i):
                    sum += L[i, k] * U[k, j] 
                U[i, j] = A[i, j] - sum
            else:
                sum = 0.0
                for k in range(j):
                    sum += L[i, k] * U[k, j]
                L[i, j] = (A[i, j] - sum) / U[j, j]

    return L, U

