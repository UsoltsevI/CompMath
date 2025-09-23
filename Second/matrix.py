import copy

#
# Приведение столбца к матрице
#
def column_to_matrix(c: list[float]) -> list[list[float]]:
    return [[c[i]] for i in range(len(c))]

#
# Приведение строки к матрице
#
def line_to_matrix(c: list[float]) -> list[list[float]]:
    return [[c[i] for i in range(len(c))]]

#
# Приведение матрицы к строке или столбцу
#
def matrix_to_line(a: list[list[float]]) -> list[float]:
    assert(len(a) == 1 or len(a[0]))

    if len(a) == 1:
        return [a[0][i] for i in range(len(a[0]))]
    else:
        return [a[i][0] for i in range(len(a))]

#
# Перемножение матрицы и матрицы
#
def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    assert(len(a) > 0)
    assert(len(b) > 0)
    assert(len(a[0]) == len(b))

    m = len(a)      # строки a
    n = len(a[0])   # столбцы a = строки b
    p = len(b[0])   # столбцы b

    c = [[0.0] * p for _ in range(m)]
    
    for i in range(m):         # по строкам a
        for j in range(p):     # по столбцам b
            for k in range(n): # общее измерение
                c[i][j] += a[i][k] * b[k][j]
    
    return c

#
# Сложение матриц
#
def sum(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    assert(len(a) > 0)
    assert(len(b) > 0)
    assert(len(a) == len(b))
    assert(len(a[0]) == len(b[0]))

    m = len(a)
    n = len(a[0])

    c = [[0.0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    
    return c

#
# Вычисление определителя матрицы
#
def determinant(a: list[list[float]]) -> float:
    assert(len(a) == len(a[0]))

    n = len(a)
    
    if n == 1:
        return a[0][0]
    elif n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    
    det = 0.0

    for j in range(n):
        # Минор матрицы
        minor = []

        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(a[i][k])
            minor.append(row)
        
        # Рекурсивный вызов и формула разложения
        det += ((-1) ** j) * a[0][j] * determinant(minor)
    
    return det

#
# Найти обратную матрицу через алгебраические дополнения"
#
def inverse(a: list[list[float]]) -> list[list[float]]:
    assert(len(a) == len(a[0]))

    n = len(a)
    det = determinant(a)
    
    if det == 0:
        raise ValueError("Матрица вырожденная, определитель равен 0")
    
    # Матрица алгебраических дополнений
    adjoint = []

    for i in range(n):
        adjoint_row = []

        for j in range(n):
            # Минор для элемента (i, j)
            minor = []

            for k in range(n):
                if k != i:
                    minor_row = []
                    for l in range(n):
                        if l != j:
                            minor_row.append(a[k][l])
                    minor.append(minor_row)
            
            # Алгебраическое дополнение
            cofactor = ((-1) ** (i + j)) * determinant(minor)
            adjoint_row.append(cofactor)

        adjoint.append(adjoint_row)
    
    # Транспонируем (присоединенная матрица)
    adjoint = list(map(list, zip(*adjoint)))
    
    # Делим на определитель
    inverse = []

    for i in range(n):
        inverse_row = []

        for j in range(n):
            inverse_row.append(adjoint[i][j] / det)

        inverse.append(inverse_row)
    
    return inverse


#
# Умножение матрицы на число
#
def multiply_k(a: list[list[float]], k: float) -> list[list[float]]:
    m = len(a)
    n = len(a[0])

    c = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] * k
    
    return c

#
# Вычислить нижнюю треугольную подматрицу а
#
def get_l(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    l = copy.deepcopy(a)

    for i in range (0, n):
        for j in range(i, n):
            l[i][j] = 0
    
    return l


#
# Вычислить верхнюю треугольную подматрицу а
#
def get_u(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    u = copy.deepcopy(a)

    for i in range (0, n):
        for j in range(0, i + 1):
            u[i][j] = 0
    
    return u


#
# Вычислить диагональную подматрицу а
#
def diag(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    d = [[0.0] * n for _ in range(0, n)]

    for i in range (1, n):
        d[i][i] = a[i][i]
    
    return d

#
# Вычисление обратной матрицы для диагональной
#
def diag_d1(d: list[list[float]]) -> list[list[float]]:
    n = len(d)
    d1 = [[0.0] * n for _ in range(0, n)]

    for i in range (1, n):
        d1[i][i] = 1 / d[i][i]
    
    return d1

