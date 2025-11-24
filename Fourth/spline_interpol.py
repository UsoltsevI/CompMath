import numpy as np
import bisect

def interpol(x, y):
    """
    Интерполяция кубическими сплайнами
    """
    a, b, c, d = calc_coefs(x, y)

    return lambda xval: calc_value(xval, x, a, b, c, d)


def calc_value(xval, x, a, b, c, d):
    """
    Вычисление значения сплайна 
    """
    i = bisect.bisect_right(x, xval)
    i = min(i, len(x) - 1)

    return a[i] + b[i] * (xval - x[i]) + 1 / 2 * c[i] * (xval - x[i]) ** 2 + 1 / 6 * d[i] * (xval - x[i]) ** 3


def calc_coefs(x, y):
    """
    Вычисление коэффициентов сплайна
    """
    n = len(x)

    M, F = create_matrices(x, y)

    c = solve_run_through(M, F)

    a = np.zeros(n)
    d = np.zeros(n)
    b = np.zeros(n)

    for i in range(n):
        hi = calc_hi(x, i)
        a[i] = y[i]
        d[i] = (c[i] - c[i - 1]) / hi
        b[i] = hi / 2 * c[i] - hi ** 2 / 6 * d[i] + (y[i] - y[i - 1]) / (hi)

    return a, b, c, d


def create_matrices(x, y):
    """
    Создание матриц для метода прогонки
    """

    n = len(x)

    M = np.zeros((n, n))
    F = np.zeros(n)

    for i in range(1, n - 1):
        hi  = calc_hi(x, i)
        hi1 = calc_hi(x, i + 1)
        M[i][i - 1] = hi
        M[i][i] = 2 * (hi + hi1)
        M[i][i + 1] = hi1
        F[i] = 6 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
    
    M[0][0] = 2 * calc_hi(x, 1)
    M[0][1] = calc_hi(x, 1)
    F[0] = 0

    M[n - 1][n - 1] = 0
    M[n - 1][n - 2] = 2 * calc_hi(x, n - 1)
    F[n - 1] = 0

    return M, F


def calc_hi(x, i):
    return x[i] - x[i - 1]

def solve_run_through(M, F):
    """
    Решение методом прогонки
    """
    n = M.shape[0]
    a = [0.0] * n
    b = [0.0] * n

    a[1] = - M[0][1] / M[0][0]
    b[1] = F[0] / M[0][0]

    for i in range(1, n - 1):
        ei = M[i][i + 1]
        di = M[i][i]
        ci = M[i][i - 1]
        
        a[i + 1] = - ei / (di + ci * a[i])
        b[i + 1] = (F[i] - ci * b[i]) / (ci * a[i] + di)
    
    x = np.zeros(n)

    cn = M[n - 1][n - 2]
    dn = M[n - 1][n - 1]

    x[n - 1] = (F[n - 1] - cn * b[n - 1]) / (cn * a[n - 1] + dn)

    for i in range(n - 2, -1, -1):
        x[i] = a[i + 1] * x[i + 1] + b[i + 1]
    
    return x

