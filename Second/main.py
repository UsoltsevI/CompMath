import equations
import gauss
import jakobi
import seidel
import grad
import min_residual
import upper_relaxation
from matrix import Matrix 

def get_x0(n: int):
    """x0 для расчётов итерационным методом"""
    x0 = Matrix(n, 1)

    for i in range(n):
        x0[i, 0] = 1

    return x0

def main():
    a, b = equations.get_matrix_y()

    print("Метод Гаусса:")
    print(gauss.solve_gauss(a, b))

    x0 = get_x0(a.rows)
    k = 100 # количество итераций

    print("Метод Якоби:")
    print(jakobi.solve_jakobi(a, b, x0, k))

    print("Метод Зейделя:")
    print(seidel.solve_seidel(a, b, x0, k))

    print("Метод верхней релаксации:")
    print(upper_relaxation.solve_upper_relaxation(a, b, x0, k))

    print("Метод градиентного спуска:")
    print(grad.solve_grad(a, b, x0, k))

    print("Метод минимальных невязок:")
    print(min_residual.solve_min_residual(a, b, x0, k))

main()
