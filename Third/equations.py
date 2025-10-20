import math
import sys
import os
# Получаем абсолютный путь к соседней папке Second
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
other_dir = os.path.join(parent_dir, 'Second')

# Добавляем в Python path
sys.path.insert(0, other_dir)
from matrix import Matrix

def func_l(x: float) -> float:
    """
    Функция для уравнения IV.12.3 (л)

    x * 2^x - 1 = 0
    """
    return x * (2 ** (x)) - 1

def func_l_der(x: float) -> float:
    """
    Производная для 
    (x * 2^x - 1)' = 2^x + x ln(2) 2^x
    """
    return 2 ** x + x * math.log(2) * 2 ** x

def phi_func_l(x: float) -> float:
    """
    Функция для МПИ x * 2^x - 1 = 0
    """
    return 1 / (2 ** x)

def func_k(x: float) -> float:
    """
    Функция для уравнения IV.12.3 (к)

    ln(x) + (x - 1)^3 = 0
    """
    return math.log(x) + (x - 1) ** 3

def func_k_der(x: float) -> float:
    """
    Прозводная для 
    (ln(x) + (x - 1)^3)' = 1/x + 3(x - 1)^2
    """
    return 1 / x + 3 * (x - 1) ** 2
    
def phi_func_k(x: float) -> float:
    """
    Функция для МПИ
    ln(x) + (x - 1)^3 = 0
    """
    return math.exp(- (x - 1) ** 3)

def system_v(xy: Matrix) -> Matrix:
    """
    Система нелинейных уравнений IV.12.4 (в)

    cos(x - 1) + y - 0.5 = 0 (f1)
    x - cosy - 3 = 0 (f2)

    Возвращает [f1, f2] в точке xy
    """
    x = xy[0, 0]
    y = xy[1, 0]

    return Matrix(2, 1, [math.cos(x - 1) + y - 0.5, 
                         x - math.cos(y) - 3])

def system_v_jakobian(xy: Matrix) -> Matrix:
    """
    Якобиан для системы 

    cos(x - 1) + y - 0.5 = 0
    x - cosy - 3 = 0

    в точке xy.

    Производные вычисляются аналитически
    """
    x = xy[0, 0]
    y = xy[1, 0]

    return Matrix(2, 2, [- math.sin(x - 1), 1, 
                         1, math.sin(y)])

def phi_system_v(xy: Matrix) -> Matrix:
    """
    Вычисление МПИ для системы 

    cos(x - 1) + y - 0.5 = 0
    x - cosy - 3 = 0
    """
    x = xy[0, 0]
    y = xy[1, 0]

    x1 = 3 + math.cos(y)
    y1 = 0.5 - math.cos(x - 1)

    return Matrix(2, 1, [x1, y1])

def get_system_v_x0() -> Matrix:
    return Matrix(2, 1, [3, 1])

def system_d(xy: Matrix) -> Matrix:
    """
    Система нелинейных уравнений IV.12.6 (д) 
    
    x^{7} - 5 x^2 y^4 + 1510 = 0
    y^3 - 3 x^4 y - 105 = 0 

    Возвращает [f1, f2] в точке xy
    """
    x = xy[0, 0]
    y = xy[1, 0]

    return Matrix(2, 1, [x ** 7 - 5 * x ** 2 * y ** 4 + 1510, 
                         y ** 3 - 3 * x ** 4 * y - 105])

def system_d_jakobian(xy: Matrix) -> Matrix:
    """
    Якобиан для системы 

    x^{7} - 5 x^2 y^4 + 1510 = 0
    y^3 - 3 x^4 y - 105 = 0

    в точке xy.

    Производные вычисляются аналитически
    """
    x = xy[0, 0]
    y = xy[1, 0]

    return Matrix(2, 2, [7 * x ** 6 - 10 * x * y ** 4, - 20 * x ** 2 * y ** 3,
                         -12 * x ** 3 * y, 3 * y ** 2 - 3 * x ** 4])

def phi_system_d(xy: Matrix) -> Matrix:
    print("НЕ НАЙДЕНА!")
    return ""
#     """
#     Вычисление МПИ для системы 

#     x^{7} - 5 x^2 y^4 + 1510 = 0
#     y^3 - 3 x^4 y - 105 = 0
#     """
#     x = xy[0, 0]
#     y = xy[1, 0]

#     # x1 = ((y ** 3 - 105) / (3 * y)) ** (1 / 4)
#     # y1 = ((x ** 7 + 1510) / (5 * x ** 2)) ** (1 / 4)

#     x1 = ((y ** 3 - 105) / (3 * y)) / (x ** 3)
#     y1 = ((x ** 7 + 1510) / (5 * x ** 2)) / (y ** 3)

#     return Matrix(2, 1, [x1, y1])
    
def get_system_d_x0() -> Matrix:
    return Matrix(2, 1, [-2, -3])