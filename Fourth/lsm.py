import numpy as np

def interpol(x, y, phi, w = []):
    """
    Интерполяция Методом Наименьших Квадратов

    phi - фнукции, из которых строим обобщённый многочлен
    w - веса точек 
    """
    n = len(x)

    if len(w) == 0:
        w = np.ones(n)

    
    A = calc_coefs(x, y, phi, w)

    return lambda xval: calc_val(xval, phi, A)

def calc_val(xval, phi, A):
    """
    Посчитать значение обобщённого многочлена с 
    коэффициентами A в точке xval
    """
    m = len(phi)
    sum = np.float64(0)

    for i in range(m):
        sum += A[i] * phi[i](xval)
    
    return sum

def calc_coefs(x, y, phi, w):
    """
    Посчитать коэффициенты А
    """
    B = create_matrix(x, phi, w)
    C = create_c(x, y, phi, w)

    return np.linalg.solve(B, C)


def scalar_mul(f1, f2, w):
    """
    Скалярное умножение f1 и f2
    """

    sum = np.float64(0)

    for i in range(len(f1)):
        sum += f1[i] * f2[i] * w[i]
    
    return sum

def create_matrix(x, phi, w):
    """
    Создать матрицу Грамма
    """
    m = len(phi)

    B = np.zeros((m, m), dtype=np.float64)

    for i in range(m):
        for j in range(i + 1):
            phi1 = calc_func_val(phi[i], x)
            phi2 = calc_func_val(phi[j], x)
            B[i][j] = scalar_mul(phi1, phi2, w)
            B[j][i] = B[i][j]
    
    return B


def create_c(x, y, phi, w):
    """
    Создать столбец c
    """
    m = len(phi)

    C = np.zeros(m)

    for i in range(m):
        phi1 = calc_func_val(phi[i], x)
        C[i] = scalar_mul(y, phi1, w)
    
    return C

def calc_func_val(func, x):
    """
    посчитать значения функции с точках x
    """
    n = len(x)
    f = np.zeros(n, dtype=np.float64)

    for i in range(n):
        f[i] = func(x[i])
    
    return f


