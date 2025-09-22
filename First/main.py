import matplotlib.pyplot as plt
from typing import Callable
import math
import numpy as np
from functions import *
from formuls import *

#
# Построение графика из 5ти линий
#
def make_graph(x: list[float], ys: list[list[float]], f_name: str = ""):
    plt.plot(x, ys[0], label='Diff 1')
    plt.plot(x, ys[1], label='Diff 2')
    plt.plot(x, ys[2], label='Diff 3')
    plt.plot(x, ys[3], label='Diff 4')
    plt.plot(x, ys[4], label='Diff 5')

    plt.legend()
    plt.xlabel('h')
    plt.ylabel('Error')
    plt.title("Зависимость абсолютной ошибки от шара дифференцирования, " + f_name)
    plt.show()


#
# Вычисление ошибки при заданных x и h
#
def calc_error(f: Callable[[float], float],
                diff_f: Callable[[Callable[[float], float], float, float], float],
                real_d: Callable[[float], float],
                x: float,
                h: float) -> float:
    return math.fabs(diff_f(f, x, h) - real_d(x))


#
# Вычисление абсолютной усрёднённой по х ошибки в зависимости от h 
#
def calc_error_array(f: Callable[[float], float],
                diff_f: Callable[[Callable[[float], float], float, float], float],
                real_d: Callable[[float], float],
                x: list[float],
                h: list[float]) -> list[float]:
    return [np.average([calc_error(f, diff_f, real_d, xi, hi) for xi in x]) for hi in h]


#
# Вычисления и построение графика ошибок для заданной функции 
# и её производной
#
def cacl_and_make_graph(f: Callable[[float], float],
                        real_d: Callable[[float], float],
                        x: list[float],
                        f_name: str = "") -> None:
    h: list[float] = [1 / 2 ** n for n in range(1, 22)]

    ys: list[list[float]] = [
        calc_error_array(f, diff_1, real_d, x, h),
        calc_error_array(f, diff_2, real_d, x, h),
        calc_error_array(f, diff_3, real_d, x, h),
        calc_error_array(f, diff_4, real_d, x, h),
        calc_error_array(f, diff_5, real_d, x, h)]

    make_graph(h, ys, f_name)

#
# Комментарий для красоты
#
def main():
    # Массив для усреднения по х
    x: list[float] = np.arange(0, 100, 0.1)

    # Строим графики
    cacl_and_make_graph(sin_x2, sin_x2_d, x, 'sin(x^2)')
    cacl_and_make_graph(cos_sin, cos_sin_d, x, 'cos(sin(x))')
    cacl_and_make_graph(exp_sin_cos, exp_sin_cos_d, x, 'exp(sin(cos(x)))')
    cacl_and_make_graph(ln_x_3, ln_x_3_d, x, 'ln(x + 3)')
    cacl_and_make_graph(sqrt_x_3, sqrt_x_3_d, x, '(x + 3)^(0.5)')

main()