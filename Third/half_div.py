
def solve_half_div(f, a, b, eps) -> list[float]:
    """
    Найти все корни f на отрезке [a0, b0] 
    методом половинного деления. k - количество итераций.
    """

    ab2 = (a + b) / 2

    if (b - a <= eps):
        return [ab2]
    

    fa = f(a)
    fb = f(b)
    fab2 = f(ab2)

    ans = []

    if (fab2 == 0):
        ans += [ab2]

    if (fab2 * fa < 0):
        ans += solve_half_div(f, a, ab2, eps)
    
    if (fab2 * fb < 0):
        ans += solve_half_div(f, ab2, b, eps)

    if (fa * fb > 0 and fa * fab2 > 0):
        return []
    
    return ans
