import copy

class Matrix:
    """Класс матриц"""

    def __init__(self, rows, cols, data=None):
        """
        Конструктор матрицы
        
        Args:
            rows: количество строк
            cols: количество столбцов
            data: список элементов (опционально)
        """
        self.rows = rows
        self.cols = cols
        
        if data:
            if len(data) != rows * cols:
                raise ValueError("Количество элементов не соответствует размеру матрицы")
            self.data = data[:]  # копируем данные
        else:
            self.data = [0.0] * (rows * cols)  # матрица нулей

    def __getitem__(self, index: tuple[int, int]):
        """Получение элемента по индексам [i][j]"""

        i, j = index

        if not (0 <= i < self.rows and 0 <= j < self.cols):
            raise IndexError("Индекс вне диапазона")
        
        return self.data[i * self.cols  + j]
    
    def __setitem__(self, index: tuple[int, int], value: float):
        """Установка элемента по индексам [i, j]"""

        i, j = index

        if not (0 <= i < self.rows and 0 <= j < self.cols):
            raise IndexError("Индекс вне диапазона")
        
        self.data[i * self.cols + j] = value

    def __add__(self, other):
        """Сложение матриц"""

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        
        result = Matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] + other[i, j]

        return result
    
    def __sub__(self, other):
        """Вычитание матриц"""

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одного размера")
        
        result = Matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] - other[i, j]

        return result
    
    def __mul__(self, other):
        """Умножение матрицы на число или на другую матрицу"""

        if isinstance(other, (int, float)):
            # Умножение на скаляр
            result = Matrix(self.rows, self.cols)

            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] * other

            return result
        
        elif isinstance(other, Matrix):
            # Умножение матриц

            if self.cols != other.rows:
                raise ValueError("Количество столбцов первой матрицы должно равняться количеству строк второй")
            
            result = Matrix(self.rows, other.cols)

            for i in range(self.rows):
                for j in range(other.cols):
                    sum_val = 0
                    for k in range(self.cols):
                        sum_val += self[i, k] * other[k, j]
                    result[i, j] = sum_val

            return result
        
    def __matmul__(self, other):
        """Умножение матриц через оператор @"""

        return self * other
    
    def transpose(self):
        """Транспонирование матрицы"""

        result = Matrix(self.cols, self.rows)

        for i in range(self.rows):
            for j in range(self.cols):
                result[j, i] = self[i, j]

        return result
    
    def __eq__(self, other):
        """Проверка на равенство матриц"""

        if not isinstance(other, Matrix):
            return False
        
        if self.rows != other.rows or self.cols != other.cols:
            return False
        
        return self.data == other.data
    
    def __str__(self):
        """Строковое представление матрицы"""

        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(str(self[i, j]))
            result.append("  ".join(row))

        return "\n".join(result)
    
    def copy(self):
        """Создание копии матрицы"""

        return Matrix(self.rows, self.cols, self.data)
    
    def identity(size):
        """Создание единичной матрицы (статический метод)"""

        matrix = Matrix(size, size)

        for i in range(size):
            matrix[i, i] = 1
        
        return matrix
    
    def zeros(rows, cols):
        """Создание матрицы нулей (статический метод)"""

        return Matrix(rows, cols)
    
    def minor(self, row, col):
        """
        Получить минор матрицы (матрица без указанной строки и столбца)
        
        Args:
            row: индекс строки для исключения
            col: индекс столбца для исключения
        
        Returns:
            Matrix: минорная матрица
        """
        if self.rows != self.cols:
            raise ValueError("Минор можно вычислить только для квадратной матрицы")
        
        if self.rows < 2:
            raise ValueError("Матрица должна быть至少 2x2 для вычисления минора")
        
        minor_data = []
        for i in range(self.rows):
            if i == row:
                continue
            for j in range(self.cols):
                if j == col:
                    continue
                minor_data.append(self[i, j])
        
        return Matrix(self.rows - 1, self.cols - 1, minor_data)

    
    def determinant(self) -> float:
        """Вычисление определителя матрицы"""

        assert(self.rows == self.cols)

        if self.rows == 1:
            return self[0, 0]
        elif self.rows == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]
        elif self.rows == 3:
            return (self[0, 0] * self[1, 1] * self[2, 2] +
                    self[0, 1] * self[1, 2] * self[2, 0] +
                    self[0, 2] * self[1, 0] * self[2, 1] -
                    self[0, 2] * self[1, 1] * self[2, 0] -
                    self[0, 1] * self[1, 0] * self[2, 2] -
                    self[0, 0] * self[1, 2] * self[2, 1])
        det = 0.0

        for j in range(self.cols):
            minor = self.minor(0, j)
            sign = 1 if j % 2 == 0 else -1
            det += sign * self[0, j] * minor.determinant()
        
        return det
    
    def algebraic_complement(self, i, j):
        """
        Вычислить алгебраическое дополнение элемента
        
        Args:
            i: индекс строки
            j: индекс столбца
        
        Returns:
            float: алгебраическое дополнение Aij
        """

        if self.rows != self.cols:
            raise ValueError("Алгебраическое дополнение можно вычислить только для квадратной матрицы")
        
        minor = self.minor(i, j)

        sign = 1 if (i + j) % 2 == 0 else -1

        return sign * minor.determinant()
    
    def cofactor_matrix(self):
        """
        Найти матрицу алгебраических дополнений (союзную матрицу)
        
        Returns:
            Matrix: матрица алгебраических дополнений
        """

        if self.rows != self.cols:
            raise ValueError("Матрица алгебраических дополнений определена только для квадратных матриц")
        
        result = Matrix(self.rows, self.cols)
        
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self.algebraic_complement(i, j)
        
        return result
    
    def adjugate(self):
        """
        Найти присоединенную матрицу (транспонированную матрицу алгебраических дополнений)
        
        Returns:
            Matrix: присоединенная матрица
        """
        return self.cofactor_matrix().transpose()
    
    def inverse(self):
        """
        Найти обратную матрицу
        
        Returns:
            Matrix: обратная матрица
        """

        det = self.determinant()

        if det == 0:
            raise ValueError("Матрица вырождена, обратной матрицы не существует")
        
        adj = self.adjugate()
        return adj * (1 / det)
    
    def get_l(self):
        """Вычислить нижнюю треугольную подматрицу"""

        assert(self.rows == self.cols)
        
        l = Matrix(self.rows, self.cols)

        for i in range (1, self.rows):
            for j in range(0, i):
                l[i, j] = self[i, j]
        
        return l

    def get_u(self):
        """Вычислить верхнюю треугольную подматрицу"""

        assert(self.rows == self.cols)
      
        u = Matrix(self.rows, self.cols)

        for i in range(0, self.rows - 1):
            for j in range(i + 1, self.cols):
                u[i, j] = self[i, j]
        
        return u
    
    def diag(self):
        """Вычислить диагональную подматрицу"""

        assert(self.rows == self.cols)

        d = Matrix(self.cols, self.rows)

        for i in range(0, self.rows):
            d[i, i] = self[i, i]
        
        return d


    
    
#
# Приведение столбца к матрице
#
def column_to_matrix(c: list[float]) -> list[list[float]]:
    return [[c[i]] for i in range(len(c))]

#
# Приведение строки к матрице
#
def line_to_matrix(c: list[float]) -> list[list[float]]:
    return [[c[i] for i in range(len(c))]]

#
# Приведение матрицы к строке или столбцу
#
def matrix_to_line(a: list[list[float]]) -> list[float]:
    assert(len(a) == 1 or len(a[0]))

    if len(a) == 1:
        return [a[0][i] for i in range(len(a[0]))]
    else:
        return [a[i][0] for i in range(len(a))]
