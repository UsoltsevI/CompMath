import copy
import numpy as np

#
# Решение уравнения Ax = b методом Гаусса
#
# Метод Гаусса заключается в приведении матрицы
# к треугольной путём сложения строк, умноженных на коэффициенты.
# Сложность: O(n^3)
#
def solve_gauss(a: list[list[float]], b: list[float]) -> list[float]:
    assert(len(a) > 0)
    assert(len(a) == len(b) and len(a[0]) == len(b))

    # Копируем чтобы не портить исходные данные
    a_copy = copy.deepcopy(a)
    b_copy = b.copy()
    n = len(a)

    # Приводим матрицу к треугольному виду
    for i in range(0, n):
        j = -1
        # Ищем первую строку с ненулевым i-м коэффициентом
        for p in range(i, n):
            if (a_copy[p][i] != 0):
                j = p
                break

        # Если такой строчки нет, то идём дальше
        
        if (j != -1):
            if (j != i):
                # Меняем местами i-ую и j-ую строчки
                a_copy[j], a_copy[i] = a_copy[i], a_copy[j]
                b_copy[j], a_copy[i] = b_copy[i], b_copy[j]

            a_ii = a_copy[i][i]

            for k in range(i + 1, n):
                if (a_copy[k][i] != 0.0):
                    coef: float = a_copy[k][i] / a_ii

                    for p in range(0, n):
                        a_copy[k][p] = a_copy[k][p] - a_copy[i][p] * coef

                    b_copy[k] = b_copy[k] - b_copy[i] * coef

    # Массив х для записи ответа 
    x = np.empty(n, dtype=float)

    # Теперь вычисляем x
    for i in range(n - 1, -1, -1):
        num = b_copy[i]

        for k in range(n - 1, i, -1):
            num -= a_copy[i][k] * x[k]

        x[i] = num / a_copy[i][i]

    return x
