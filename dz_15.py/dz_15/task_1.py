"""
Создайте класс Матрица. Добавьте методы для:
-вывода на печать,
-сравнения,
-сложения,
-*умножения матриц
"""

import logging

logging.basicConfig(filename='log_1.log',
                    filemode='w', encoding='utf-8',
                    format='{levelname:<6} - {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{', level=logging.INFO)
logger = logging.getLogger(__name__)