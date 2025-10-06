import equations
import gauss
import lu
import jakobi
import seidel
import grad
import min_residual
import upper_relaxation
from matrix import Matrix 
import time
import math
import csv
import matplotlib.pyplot as plt

def get_x0(n: int):
    """x0 для расчётов итерационным методом"""
    x0 = Matrix(n, 1)

    for i in range(n):
        x0[i, 0] = 1

    return x0

def make_residual_plot(rk_arr: list[float], f_name: str = ""):
    plt.figure(figsize=[12, 8])
    plt.plot([i + 1 for i in range(len(rk_arr))], rk_arr, label='Невязка')

    plt.legend()
    plt.xlabel('k')
    plt.ylabel('r')
    plt.title("Зависимость невязки от итерации, " + f_name)
    plt.show()

def make_residual_log_plot(rk_arr: list[float], f_name: str = ""):
    plt.figure(figsize=[12, 8])
    plt.plot([math.log(i + 1) for i in range(len(rk_arr))], [math.log(rk_arr[i]) for i in range(len(rk_arr))], label='Невязка')

    plt.legend()
    plt.xlabel('log(k)')
    plt.ylabel('log(r)')
    plt.title("Зависимость невязки от итерации, " + f_name)
    plt.show()

def calculate(func) -> tuple[float, Matrix]:
    """Вызвать функцию и замерить вермя выполнения"""
    start_time = time.time()  
    result = func["func"]() 
    end_time = time.time()  
    return end_time - start_time, result


def calc_error(x1: Matrix, x2: Matrix) -> float:
    """Вычислить разницу как корень из суммы квадратов (x1_i - x2_i)"""
    sum = 0.0
    for i in range(x1.rows):
        sum += (x1[i, 0] - x2[i, 0]) ** 2
    return math.sqrt(sum)


def main():
    a, b = equations.get_matrix_y()

    x0 = get_x0(a.rows)
    k = 100 # количество итераций

    functions = [{
        "name": "gauss",
        "title": "Метод Гаусса",
        "func": lambda:  gauss.solve_gauss(a, b),
        "iterative": False,
    }, {
        "name": "lu",
        "title": "Метод LU-разложения",
        "func": lambda: lu.solve_lu(a, b),
        "iterative": False,
    }, {
        "name": "jakobi",
        "title": "Метод Якоби",
        "func": lambda: jakobi.solve_jakobi(a, b, x0, k),
        "iterative": True,
    }, {
        "name": "seidel",
        "title": "Метод Зейделя",
        "func": lambda: seidel.solve_seidel(a, b, x0, k),
        "iterative": True,
    }, {
        "name": "up_rel",
        "title": "Метод верхней релаксации",
        "func": lambda: upper_relaxation.solve_upper_relaxation(a, b, x0, k),
        "iterative": True,
    }, {
        "name": "grad",
        "title": "Метод градиентного спуска",
        "func": lambda: grad.solve_grad(a, b, x0, k),
        "iterative": True,
    }, {
        "name": "min_res",
        "title": "Метод минимальных невязок",
        "func": lambda: min_residual.solve_min_residual(a, b, x0, k),
        "iterative": True,
    }]

    gauss_result = gauss.solve_gauss(a, b)

    results = []
    
    for func in functions:
        ex_time, ans = calculate(func)

        if func["iterative"]:
            make_residual_plot(ans[1], func["title"])
            make_residual_log_plot(ans[1], func["title"])
            ans = ans[0]

        error = calc_error(ans, gauss_result)

        results.append([
            func["name"],
            func["title"],
            ex_time,
            # ans,
            error,
        ] + [ans[i, 0] for i in range(ans.rows)])

    
    # Запись в CSV
    with open('results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "title", "ex_time", "error"] + ["x" + str(i) for i in range(a.rows)])
        writer.writerows(results)

main()
