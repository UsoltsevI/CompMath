
def interpol_newton(x, y):
    """
    Интерполяция полиномом Ньютона.

    Возвращает функцию полинома
    """

    coefs = calc_coefs(x, y)

    return lambda xval: calc_value(xval, x, coefs)

def calc_value(xval, x, coefs):
    """
    Посчитать значение полинома Ньютона в точке xval
    """

    sum = 0.0
    mul = 1

    for i in range(len(coefs)):
        sum += coefs[i] * mul
        mul *= (xval - x[i])
    
    return sum
    

def calc_coefs(x, y):
    """
    Вычисление коэффициентов для полинома Ньютона
    """
    n = len(x)

    coefs = [0.0] * n
    div_diffs = y.copy()

    coefs[0] = div_diffs[0]

    for i in range(1, n):
        calc_next_div_diffs(x, div_diffs)
        coefs[i] = div_diffs[0]
    
    return coefs


def calc_next_div_diffs(x, dd):
    k = len(x) - len(dd) + 1

    for i in range(len(dd) - 1):
        dd[i] = div_diff(dd[i], dd[i + 1], x[i], x[i + k])
    
    dd.pop(len(dd) - 1)

    return dd



def div_diff(f1, f2, x1, x2):
    """
    Разделённая разность
    """

    return (f2 - f1) / (x2 - x1)
