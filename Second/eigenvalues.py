import math
from matrix import Matrix

def power_iteration(A: Matrix, x0: Matrix, k: int = 1000) -> float:
    """
    Находит наибольшее по модулю собственное значение и соответствующий 
    собственный вектор с помощью степенного метода.
    """
    n = A.rows
    
    if A.rows != A.cols:
        raise ValueError("Матрица должна быть квадратной")
    
    x_k = x0
    x_k = x_k * (1 / norm_l2(x_k))  # Нормировка
    
    eigenvalue = 0.0

    for i in range(k):
        Ax = A * x_k
        
        # Вычисление текущей оценки собственного значения
        # (xᵀ * A * x) / (xᵀ * x), но так как x нормирован, xᵀ*x = 1
        eigenvalue = x_k.transpose() * Ax
        
        # Нормализация нового вектора
        x_new = Ax * (1 / norm_l2(Ax))
        
        x_k = x_new
    
    return eigenvalue[0, 0]


def norm_l2(x: Matrix) -> float:
    """Нахождение нормы вектора по L2"""
    sum = 0.0
    for i in range(x.rows):
        sum += x[i, 0] ** 2
    return math.sqrt(sum)