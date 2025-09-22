import numpy as np

def sin_x2(x: float) -> float:
    return np.sin(x * x)

def sin_x2_d(x: float) -> float:
    return np.cos(x * x) * 2 * x


def cos_sin(x: float) -> float:
    return np.cos(np.sin(x))

def cos_sin_d(x: float) -> float:
    return - np.sin(np.sin(x)) * np.cos(x)


def exp_sin_cos(x: float) -> float:
    return np.exp(np.sin(np.cos(x)))

def exp_sin_cos_d(x: float) -> float:
    return np.exp(np.sin(np.cos(x))) * np.cos(np.cos(x)) * np.sin(x)


def ln_x_3(x: float) -> float:
    return np.log(x + 3)

def ln_x_3_d(x: float) -> float:
    return 1 / (x + 3)


def sqrt_x_3(x: float) -> float:
    return (x + 3)**(0.5)

def sqrt_x_3_d(x: float) -> float:
    return (x + 3) ** (-0.5) * 0.5

