
def integrate(f, x):
    """
    Вычисление интеграла методом 
    правых прямоугольников.
    """
    n = len(x)

    sum = 0.0

    for i in range(n - 1):
        sum += (x[i + 1] - x[i]) * f[i]

    return sum 

def get_graph_data(f, x):
    fc = [f[0]]
    xc = [x[0]]

    for i in range(1, len(x)):
        xc.append(x[i])
        fc.append(f[i - 1])
        xc.append(x[i])
        fc.append(f[i])
    
    return fc, xc



        