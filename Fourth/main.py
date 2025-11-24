from data import getSingapureData
# from testData import getTestData
import matplotlib.pyplot as plt
import interpol_newton as newton
import numpy as np
import spline_interpol as spline

def main():
    years, population = getSingapureData()
    # years, population = getTestData()

    # newton_func = newton.interpol_newton(years, population)

    # xs = np.arange(years[0], years[-1] + 1, 1)

    # plt.figure(figsize=[15,8])
    # plt.plot(years, population, '.')
    # plt.plot(xs, newton_func(xs), '-')
    # plt.title("Singapure population")
    # plt.xlabel("Year")
    # plt.ylabel("Population")
    # plt.grid()
    # plt.show()

    spline_func = spline.interpol(years, population)

    xs = np.arange(years[0], years[-1] + 1, 1)

    plt.figure(figsize=[15,8])
    plt.plot(years, population, '.')
    plt.plot(xs, [spline_func(xsi) for xsi in xs], '-')
    plt.title("Singapure population (Spline)")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid()
    plt.show()



main()

