from matrix import Matrix


def solve_gauss(a: Matrix, b: Matrix) -> Matrix:
    """
    Решение уравнения Ax = b методом Гаусса
    
    Метод Гаусса заключается в приведении матрицы
    к треугольной путём сложения строк, умноженных на коэффициенты.
    Сложность: O(n^3)
    """
    
    # Копируем чтобы не портить исходные данные
    a_copy = a.copy()
    b_copy = b.copy()
    n = a.rows

    # Приводим матрицу к треугольному виду
    for i in range(0, n):
        j = -1
        # Ищем первую строку с ненулевым i-м коэффициентом
        for p in range(i, n):
            if (a_copy[p, i] != 0):
                j = p
                break

        # Если такой строчки нет, то идём дальше
        
        if (j != -1):
            if (j != i):
                # Меняем местами i-ую и j-ую строчки
                for p in range(0, n):
                    a_copy[j, p], a_copy[i, p] = a_copy[i, p], a_copy[j, p]
                
                b_copy[j], a_copy[i] = b_copy[i], b_copy[j]

            a_ii = a_copy[i, i]

            for k in range(i + 1, n):
                if (a_copy[k, i] != 0.0):
                    coef: float = a_copy[k, i] / a_ii

                    for p in range(0, n):
                        a_copy[k, p] = a_copy[k, p] - a_copy[i, p] * coef

                    b_copy[k, 0] = b_copy[k, 0] - b_copy[i, 0] * coef

    # Массив х для записи ответа 
    x = Matrix(n, 1)

    # Теперь вычисляем x
    for i in range(n - 1, -1, -1):
        num = b_copy[i, 0]

        for k in range(n - 1, i, -1):
            num -= a_copy[i, k] * x[k, 0]

        x[i, 0] = num / a_copy[i, i]

    return x
