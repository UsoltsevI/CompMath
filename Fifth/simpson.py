import numpy as np
import bisect

def integrate(f, x):
    """
    Интегрирование методом Симпсона
    """
    n = len(x)

    sum = 0.0

    for i in range(0, n - 1, 2):
        h1 = x[i + 1] - x[i]
        h2 = x[i + 2] - x[i + 1]
        sum += (h1 + h2) / 6 * ((2 - h2 / h1) * f[i] + (h1 + h2) ** 2 / (h1 * h2) * f[i + 1] + (2 - h1 / h2) * f[i + 2])

    return sum

def get_func(f, x):
    n = len(x)

    funcs = []

    for i in range(0, n - 1, 2):
        parabola = np.poly1d(np.polyfit(x[i:(i + 3)], f[i:(i + 3)], 2))
        funcs.append(parabola)
        funcs.append(parabola)

    return lambda xval: get_value(funcs, x, xval)

def get_value(funcs, x, xval):
    idx = bisect.bisect_left(x, xval)
    return funcs[max(idx - 1, 0)](xval)

