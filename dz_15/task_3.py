"""
Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""

from math import factorial
import logging

logging.basicConfig(filename='log_3.log',
                    filemode='w', encoding='utf-8',
                    format='{levelname:<6} - {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{', level=logging.INFO)
logger = logging.getLogger(__name__)


class Factorial:

    def __init__(self, count: int = 1) -> None:
        self.history = []
        self.count = count

    def __call__(self, n: int = 1) -> list[int]:
        if n < 0:
            logger.error(f'Число n не может быть отрицательным: {n}')
            raise ValueError("Incompatible value")
        res = factorial(n)
        self.history.append({n: res})
        self.history = self.history[-self.count:]
        logger.info(f'factorial({n}) = {res}')
        return res

    def get_history(self):
        return self.history


if __name__ == '__main__':
    f = Factorial(3)
    for i in range(1, 11):
        print(f'{i}! = {f(i)}')

    print(f'{-1}! = {f(-1)}')

    print(f.get_history())
