"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""

import logging

logging.basicConfig(filename='log_2.log',
                    filemode='w', encoding='utf-8',
                    format='{levelname:<6} - {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{', level=logging.INFO)
logger = logging.getLogger(__name__)


class RectangleSideError(Exception):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            logger.error(f'Ошибка ввода: обе стороны имеют невалидные значения = {self.a}; {self.b}')
            return f"Ошибка ввода: обе стороны имеют невалидные значения = {self.a}; {self.b}"
        else:
            if self.a <= 0:
                logger.error(f'Ошибка ввода: сторона имеет невалидное  значение = {self.a}')
                return f"Ошибка ввода: сторона имеет невалидное  значение = {self.a} "
            else:
                logger.error(f'Ошибка ввода: сторона имеет невалидное  значение  = {self.b}')
                return f"Ошибка ввода: сторона имеет невалидное  значение  = {self.b}"


class Rectangle:
    """
    Класс прямоугольник.
    Имеет возможность сложения и вычитания.
    """

    def __init__(self, side_a, side_b=0.0):
        """
        Инициализирует экземпляр
        :param side_a:
        :param side_b:
        """
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

        if side_a <= 0 or side_b <= 0:
            raise RectangleSideError(side_a, side_b)

    def get_perimeter(self):
        """
        Возвращает периметр прямоугольника
        :return int
        """
        logger.info(f'Периметр Rectangle({self.side_a},{self.side_b}) равен {2 * (self.side_a + self.side_b)}')
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        """
        Возвращает площадь прямоугольника
        :return int
        """
        logger.info(f'Площадь Rectangle({self.side_a},{self.side_b}) равна {(self.side_a * self.side_b)}')
        return self.side_a * self.side_b

    def __add__(self, other):
        """
        Функция складывает данный прямоугольник с другим
        :param other - другой прямоугольник
        :return Rectangle - новый прямоугольник
        """
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        logger.info(
            f'Rectangle({self.side_a},{self.side_b}) + Rectangle({other.side_a},{other.side_b}) '
            f'= Rectangle({Rectangle(res).side_a},{Rectangle(res).side_b})')
        return Rectangle(res)

    def __sub__(self, other):
        """
        Функция отнимает из данного прямоугольника другой
        :param other - другой прямоугольник
        :return Rectangle - новый прямоугольник
        """
        res = abs(self.get_perimeter() - other.get_perimeter())
        logger.info(
            f'Rectangle({self.side_a},{self.side_b}) - Rectangle({other.side_a},{other.side_b}) '
            f'= Rectangle({Rectangle(res).side_a},{Rectangle(res).side_b})')
        return Rectangle(res)

    def __eq__(self, other):  # равно ==
        """
        Функция сравнивает на равенство данный прямоугольник с другим
        :param other - другой прямоугольник
        :return Boolean - True если условие выполняется и False усли нет
        """
        logger.info(
            f'Rectangle({self.side_a},{self.side_b}) '
            f'{"=" if self.get_area() == other.get_area() else "!="} Rectangle({other.side_a},{other.side_b})')
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # неравно !=
        """
        Функция сравнивает на неравенство данный прямоугольник с другим
        :param other - другой прямоугольник
        :return Boolean - True если условие выполняется и False усли нет
        """
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # больше >
        """
        Функция сравнивает на больше данный прямоугольник с другим
        :param other - другой прямоугольник
        :return Boolean - True если условие выполняется и False усли нет
        """
        logger.info(
            f'Rectangle({self.side_a},{self.side_b}) '
            f'{">" if self.get_area() > other.get_area() else "<"} Rectangle({other.side_a},{other.side_b})')
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # больше или равно >=
        """
        Функция сравнивает на больше или равно данный прямоугольник с другим
        :param other - другой прямоугольник
        :return Boolean - True если условие выполняется и False усли нет
        """
        logger.info(
            f'Rectangle({self.side_a},{self.side_b}) '
            f'{"=>" if self.get_area() >= other.get_area() else "<"} Rectangle({other.side_a},{other.side_b})')
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # метод меньше <
        """
        Функция сравнивает на меньше данный прямоугольник с другим
        :param other - другой прямоугольник
        :return Boolean - True если условие выполняется и False усли нет
        """
        logger.info(
            f'Rectangle({self.side_a},{self.side_b}) '
            f'{"<" if self.get_area() < other.get_area() else ">="} Rectangle({other.side_a},{other.side_b})')
        return self.get_area() < other.get_area()

    def __le__(self, other):  # меньше или равно <=
        """
        Функция сравнивает на меньше или равно данный прямоугольник с другим
        :param other - другой прямоугольник
        :return Boolean - True если условие выполняется и False усли нет
        """
        logger.info(
            f'Rectangle({self.side_a},{self.side_b}) '
            f'{"<=" if self.get_area() <= other.get_area() else ">"} Rectangle({other.side_a},{other.side_b})')
        return self.get_area() <= other.get_area()

    def __str__(self):
        """
        Возвращает официальное текстовое представление экземпляра класса
        :return str
        """
        return f'Rectangle({self.side_a = },{self.side_b = })'

    def __repr__(self):
        """
        Возвращает официальное текстовое представление экземпляра класса
        :return str
        """
        return f'Rectangle({self.side_a = },{self.side_b = })'


rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)

print(f'площадь 1 прямоугольника = {rectangle1.get_area():.2f}')
print(f'площадь 2 прямоугольника = {rectangle2.get_area():.2f}')
# print(rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} = {rectangle2.get_area():.2f}):', rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):', rectangle1 != rectangle2)
print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):', rectangle1 > rectangle2)
print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):', rectangle1 <= rectangle2)
print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):', rectangle1 < rectangle2)
print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):', rectangle1 >= rectangle2)

print(rectangle1)
print(rectangle2)

try:
    Rectangle(-7, 3)
    Rectangle(5.6, -10.2)
    Rectangle(-13)
except RectangleSideError as exc:
    print(f'Ошибка!!! Such Rectangle can be created ! {exc}')