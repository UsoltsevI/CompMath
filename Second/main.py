import equations
import gauss
import jakobi
import seidel

#
# Бесполезный комментарий
#
def main():
    a, b = equations.get_matrix_y()

    print("Метод Гаусса:")
    print(gauss.solve_gauss(a, b))

    print("Метод Якоби:")
    print(jakobi.solve_jakobi(a, b, [1] * len(a), 100))

    print("Метод Зейделя:")
    print(seidel.solve_seidel(a, b, [1] * len(a), 100))

main()
