from typing import Callable

def diff_1(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h

def diff_2(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x) - f(x - h)) / h

def diff_3(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x - h)) / (2 * h)

def diff_4(f: Callable[[float], float], x: float, h: float) -> float:
    return ((4 / 3) * (f(x + h) - f(x - h)) / (2 * h) 
            - 1 / 3 * (f(x + 2 * h) - f(x - 2 * h)) / (4 * h))

def diff_5(f: Callable[[float], float], x: float, h: float) -> float:
    return ((3 / 2) * (f(x+ h) - f(x - h)) / (2 * h) 
            - (3 / 5) * (f(x + 2 * h) - f(x - 2 * h)) / (4 * h) 
            + (1 / 10) * (f(x + 3 * h) - f(x - 3 * h)) / (6 * h))