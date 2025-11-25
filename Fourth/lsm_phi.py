import numpy as np

def get_phi1():
    """
    Функции для обобщённого многочлена

    """
    phi = [lambda xval: 1,
            lambda xval: xval,
            # lambda xval: xval ** 2,
            # lambda xval: xval ** 3,
            # lambda xval: xval ** 4,
            # lambda xval: xval ** 5,
            # lambda xval: np.log2(xval),
            lambda xval: np.exp(xval / 1000),
            # lambda xval: np.sin(xval / 1000)
            ]

    return phi
    