import math

def solve_simple_iter(phi, x0, eps) -> float:
    """
    Решить нелинейное уравнение методом простой итерации
    """
    xk = x0
    xkp = 0

    while (math.fabs(xkp - xk) > eps):
        xkp = xk
        xk = phi(xk)
    
    return xk

def less_than_eps(x, eps):
    """
    Проверить, что все значения в столбце не превышают eps
    """
    for i in range(x.rows):
        if (math.fabs(x[i, 0]) >= eps):
            return False
    
    return True

def solve_simple_iter_matrix(phi, x0, eps) -> float:
    """
    Решить систему нелинейных уравнений МПИ
    """
    xk = x0
    xkp = xk * 10

    while not less_than_eps(xkp - xk, eps):
        xkp = xk
        xk = phi(xk)
    
    return xk
