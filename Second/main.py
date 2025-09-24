import equations
import gauss
import jakobi
import seidel
from matrix import Matrix 

def get_x0(n: int):
    x0 = Matrix(n, 1)

    for i in range(n):
        x0[i, 0] = 1

    return x0

#
# Бесполезный комментарий
#
def main():
    a, b = equations.get_matrix_y()

    print("Метод Гаусса:")
    print(gauss.solve_gauss(a, b))

    x0 = get_x0(a.rows)

    print("Метод Якоби:")
    print(jakobi.solve_jakobi(a, b, x0, 10))

    print("Метод Зейделя:")
    print(seidel.solve_seidel(a, b, x0, 100))

main()
