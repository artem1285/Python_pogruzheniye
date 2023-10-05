"""
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""

import logging

logging.basicConfig(filename='log_1.log',
                    filemode='w', encoding='utf-8',
                    format='{levelname:<6} - {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{', level=logging.INFO)
logger = logging.getLogger(__name__)


class MatrixSizeError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            logger.error(f'Невозможно сложить матрицы, матрицы разных размеров')
            return f"Error: Невозможно сложить матрицы, матрицы разных размеров"
        elif self.operation == '*':
            logger.error(f'Невозможно перемножить матрицы: не подходят размерности')
            return f"Error: Невозможно перемножить матрицы: не подходят размерности"
        else:
            logger.error(f'Невозможно сравнить. Матрицы разных размеров')
            return f"Error: Невозможно сравнить. Матрицы разных размеров"


class Matrix:
    """
    Класс Матрица.
    Он умеет выводить себя на печать, сравнивать себя с другими, складывать себя с другими и умножать.
    """
    _rows: int = None
    _cols: int = None
    _a_matrix: list[list[int, int]] = None

    def __init__(self, a_matrix: list[list[int, int]]) -> None:
        """
        Инициализация матрицы
        :param a_matrix: list    -- [row, col]
        """
        self._rows = len(a_matrix)
        self._cols = len(a_matrix[0])
        self._a_matrix = a_matrix

    def __add__(self, other) -> 'Matrix':
        """
        Сложение матриц
        :param other: Matrix    -- other Matrix object
        :return: Matrix         -- new Matrix object
        """
        if not isinstance(other, self.__class__):
            logger.error("Not a 'Matrix'-type object")
            raise TypeError("Not a 'Matrix'-type object")
        if self._rows != other._rows or self._cols != other._cols:
            raise MatrixSizeError("+")
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._a_matrix[j][i] + other._a_matrix[j][i]
        logger.info(f'{repr(self)} + {repr(other)} = {repr(Matrix(new_matrix))}')
        return Matrix(new_matrix)

    def __mul__(self, other) -> 'Matrix':
        """
        Умножение двух матриц
        :param other: [int, int, Matrix]    -- other Matrix object
        :return: Matrix                       -- new Matrix object
        """
        if isinstance(other, self.__class__):
            return self.__rmul__(other)
        elif isinstance(other, int) or isinstance(other, int):
            new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
            for j in range(self._rows):
                for i in range(self._cols):
                    new_matrix[j][i] = self._a_matrix[j][i] * other
            logger.info(f'{repr(self)} * {repr(other)} = {repr(Matrix(new_matrix))}')
            return Matrix(new_matrix)
        else:
            raise TypeError("Unsupported operation")

    def __rmul__(self, other) -> 'Matrix':
        """
        Умножение матриц
        :param other: Matrix    -- other Matrix object
        :return: Matrix         -- new Matrix object
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._cols != other._rows:
            raise MatrixSizeError("*")
        new_matrix = [[0 for _ in range(other._rows)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(other._rows):
                new_matrix[j][i] = self._a_matrix[j][i] * other._a_matrix[i][j]
        logger.info(f'{repr(self)} + {repr(other)} = {repr(Matrix(new_matrix))}')
        return Matrix(new_matrix)

    def __eq__(self, other) -> bool:
        """
        Возвращает True если передаваемая матрица равна текущей, иначе False
        :return Boolean
        """
        if self is other:
            return True
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._rows != other._rows or self._cols != other._cols:
            raise MatrixSizeError("=")
        for j in range(self._rows):
            for i in range(self._cols):
                if self._a_matrix[j][i] != other._a_matrix[j][i]:
                    logger.info(f'{repr(self)} != {repr(other)}')
                    return False
        logger.info(f'{repr(self)} = {repr(other)}')
        return True

    def __ne__(self, other) -> bool:
        """
        Возвращает True если передаваемая матрица не равна текущей, иначе False
        :return Boolean
        """
        return not self.__eq__(other)

    def __str__(self) -> str:
        """
        Возвращает официальное текстовое представление экземпляра класса.
        :return str
        """
        return '\n'.join(['\t'.join(map(str, row)) for row in self._a_matrix]) + '\n'

    def __repr__(self):
        """
        Возвращает официальное текстовое представление экземпляра класса.
        :return str
        """
        return f'Matrix({self._a_matrix})'


if __name__ == '__main__':

    mtx_a = Matrix([[4, 8, 9], [14, 5, 86], [72, 81, 19]])
    mtx_b = Matrix([[3, 5, 3], [4, 51, 61], [75, 18, 29]])
    mtx_c = Matrix([[1, 1, 2], [24, 5, 46], [1, 23, 33], [3, 81, 19]])
    mtx_d = Matrix([[21, 12, 3, 40, ], [15, 16, 71, 18], [5, 11, 1, 23]])
    print(repr(mtx_a))
    print(repr(mtx_d))
    print(mtx_a)
    print(mtx_b)
    print(mtx_c)
    print(mtx_d)

    print(f'{mtx_a == mtx_b=}')
#    print(f'{mtx_b == mtx_c=}')
    print(mtx_a * mtx_b)
    print(mtx_a + mtx_b)
#    print(mtx_a + mtx_c)

    try:
        print(f'{mtx_c != mtx_d=}')
        print(mtx_c + mtx_d)
    except MatrixSizeError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * mtx_b)
    except MatrixSizeError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * mtx_d)
    except MatrixSizeError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * 10)
    except TypeError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
