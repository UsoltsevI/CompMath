from equations import func_l, func_l_der, phi_func_l, func_k, func_k_der, phi_func_k, system_v, system_v_jakobian, phi_system_v, get_system_v_x0, system_d, system_d_jakobian
from half_div import solve_half_div
from simple_iter import solve_simple_iter, solve_simple_iter_matrix
from newton import solve_newton, solve_newton_mod, solve_newton_matrix, solve_newton_matrix_mod

def main():
    eps = 0.00001

    ans = solve_half_div(func_l, 0, 2, eps)
    print("Решение 1 методом половинного деления")
    print(ans)

    ans = solve_simple_iter(phi_func_l, 1, eps)
    print("Решение 1 МПИ")
    print(ans)

    ans = solve_newton(func_l, func_l_der, 1, eps)
    print("Решение 1 методом Ньютона")
    print(ans)

    ans = solve_newton_mod(func_l, func_l_der, 1, eps)
    print("Решение 1 модифицированным методом Ньютона")
    print(ans)

    ans = solve_half_div(func_k, 0.5, 2, eps)
    print("Решение 2 методом половинного деления")
    print(ans)

    ans = solve_simple_iter(phi_func_k, 1, eps)
    print("Решение 2 МПИ")
    print(ans)

    ans = solve_newton(func_k, func_k_der, 1, eps)
    print("Решение 2 методом Ньютона")
    print(ans)

    ans = solve_newton_mod(func_k, func_k_der, 1, eps)
    print("Решение 2 модифицированным методом Ньютона")
    print(ans)

    ans = solve_simple_iter_matrix(phi_system_v, get_system_v_x0(), eps)
    print("Решение 3 МПИ:")
    print(ans)

    ans = solve_newton_matrix(system_v, system_v_jakobian, get_system_v_x0(), eps)
    print("Решение 3 методом Ньютона:")
    print(ans)

    ans = solve_newton_matrix_mod(system_v, system_v_jakobian, get_system_v_x0(), eps)
    print("Решение 3 модифицированным методом Ньютона:")
    print(ans)

    # ans = solve_simple_iter(phi_system_d, get_system_v_x0(), 100)

    # print(ans)

    ans = solve_newton_matrix(system_d, system_d_jakobian, get_system_v_x0(), eps)
    print("Решение 4 методом Ньютона:")
    print(ans)

    ans = solve_newton_matrix_mod(system_d, system_d_jakobian, get_system_v_x0(), eps)
    print("Решение 4 модифицированным методом Ньютона:")
    print(ans)






main()