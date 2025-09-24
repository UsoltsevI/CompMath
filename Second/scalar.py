from matrix import Matrix

def mul_scalar(a: Matrix, b: Matrix) -> float:
    """
    Вычислить скалярное произведение столбцов a и b
    """
    if a.cols != 1 or b.cols != 1 or a.rows != b.rows:
        raise ValueError("Скаларно перемножать можно только стаолбы одинкаовой размерности")
    
    result = 0
    
    for i in range(a.rows):
        result += a[i, 0] * b[i, 0]
    
    return result