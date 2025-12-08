from interpol_newton import interpol_newton

def integrate(f, x, n):
    func = interpol_newton(x, f)

    xi, ci = get_coefs(n)

    sum = 0.0

    for i in range(n):
        # Растягиваем и переносим
        xa = xi[i] * (x[len(x) - 1] - x[0]) / 2 + (x[len(x) - 1] + x[0]) / 2
        sum += ci[i] * func(xa)

    return sum

def get_func(f, x):
    return interpol_newton(x, f)

def get_coefs(n):
    xi = []
    ci = []

    if n == 1:
        xi = [0]
        ci = [2]
    elif n == 2:
        xi = [-0.5773503, 0.5773503]
        ci = [1, 1]
    elif n == 3:
        xi = [-0.7745967, 0, 0.7745967]
        ci = [0.5555556, 0.8888889, 0.5555556]
    elif n == 4:
        xi = [-0.8611363, -0.3399810, 0.3399810, 0.8611363]
        ci = [0.3478548, 0.6521451, 0.6521451, 0.3478548]
    
    # Дальше лень переписывать таблицу
    #
    # Да и вообще можно было просто дёрнуть numpy, 
    # где все эти коэффициенты есть

    return xi, ci
