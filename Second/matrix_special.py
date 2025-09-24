from matrix import Matrix

def get_inversed_diag(diag: Matrix) -> Matrix:
    """
    Вычислить обратную матрицу для диагональной.
    Оптимизированный способ.
    """
    d1 = diag.copy()
    for i in range(d1.rows):
        d1[i, i] = 1 / d1[i, i]
    return d1

def inverse_lower_triangular(l: Matrix):
    """
    Вычислить обратную для нижней треугольной матрицы.
    Оптимизированный способ.
    """    

    if l.rows != l.cols:
        raise ValueError("Матрица должна быть квадратной")
    
    n = l.rows
    for i in range(n):
        if abs(l[i, i]) < 1e-12:
            raise ValueError("Матрица вырождена")
    
    # Создаем обратную матрицу (изначально нулевую)
    inv = Matrix(n, n)
    
    # Построчно вычисляем обратную матрицу
    for i in range(n):
        # Диагональный элемент обратной матрицы
        inv[i, i] = 1.0 / l[i, i]
        
        # Элементы под диагональю в текущем столбце
        for j in range(i + 1, n):
            sum_val = 0
            for k in range(i, j):
                sum_val += l[j, k] * inv[k, i]
            inv[j, i] = -sum_val / l[j, j]

    return inv