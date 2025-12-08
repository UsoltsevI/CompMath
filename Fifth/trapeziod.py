
def integrate(f, x):
    n = len(x)

    sum = 0.0

    for i in range(n - 1):
        sum += (x[i + 1] - x[i]) * (f[i] + f[i + 1]) / 2
    
    return sum