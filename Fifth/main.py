from data import get_data_94
import rectangle
import trapeziod
import matplotlib.pyplot as plt
import simpson
import gauss
import numpy as np

def main():
    x, f = get_data_94()

    # Figure 1
    fig = plt.figure(figsize=[8,20])
    plt.title("9.4")
    fig.add_subplot(2, 1, 1)
    plt.scatter(x, f)
    plt.grid()

    fig.add_subplot(2, 1, 2)
    rfc, rxc = rectangle.get_graph_data(f, x)
    plt.plot(rxc, rfc)
    plt.title("Square = " + str(rectangle.integrate(f, x)))
    plt.fill_between(rxc, rfc, [0] * len(rfc))
    plt.grid()

    # Figure 2
    fig = plt.figure(figsize=[8,12])
    fig.add_subplot(2, 1, 1)
    plt.plot(x, f)
    plt.title("Square = " + str(trapeziod.integrate(f, x)))
    plt.fill_between(x, f, [0] * len(x))
    plt.grid()

    fig.add_subplot(2, 1, 2)
    N = 512
    xarr = np.arange(N) / N * 2 
    gauss_func = gauss.get_func(f, x)
    yarr = [gauss_func(xa) for xa in xarr]
    plt.plot(xarr, yarr)
    plt.title("Square = " + str(gauss.integrate(f, x, 4)))
    plt.fill_between(xarr, yarr, [0] * len(xarr))
    plt.grid()

    fig = plt.figure(figsize=[8,6])
    simp_func = simpson.get_func(f, x)
    yarr = [simp_func(xa) for xa in xarr]
    plt.plot(xarr, yarr)
    plt.title("Square = " + str(simpson.integrate(f, x)))
    plt.fill_between(xarr, yarr, [0] * len(xarr))
    plt.grid()

    plt.tight_layout()
    plt.show()






main()

