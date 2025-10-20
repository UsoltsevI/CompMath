import math

def solve_newton(f, f_der, x0, eps):
    """
    Решить нелинейное уравнение методом Ньтона
    """
    xk = x0
    xkp = 0

    while (math.fabs(xkp - xk) > eps):
        xkp = xk
        xk = xk - f(xk) / f_der(xk)
    
    return xk

def solve_newton_mod(f, f_der, x0, eps):
    """
    Решить нелинейное уравнение модифицированным
    методом Ньтона
    """
    xk = x0
    xkp = xk * 10

    der = f_der(x0)

    while math.fabs(xk - xkp) > eps:
        xkp = xk
        xk = xk - f(xk) / der
    
    return xk

def less_than_eps(x, eps):
    """
    Проверить, что все значения в столбце не превышают eps
    """
    for i in range(x.rows):
        if (math.fabs(x[i, 0]) >= eps):
            return False
    
    return True


def solve_newton_matrix(f, f_der, x0, eps):
    """
    Решить систему нелинейных уравнений методом Ньютона
    """
    xk = x0
    xkp = xk * 10

    while not less_than_eps(xk - xkp, eps):
        xkp = xk
        xk = xk - f_der(xk).inverse() * f(xk)
    
    return xk

def solve_newton_matrix_mod(f, f_der, x0, eps):
    """
    Решить систему нелинейных уравнений 
    модифицированным методом Ньютона
    """
    xk = x0
    xkp = xk * 10

    der = f_der(x0).inverse()

    while not less_than_eps(xk - xkp, eps):
        xkp = xk
        xk = xk - der * f(xk)
    
    return xk
