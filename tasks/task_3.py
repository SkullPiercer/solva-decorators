# ЗАДАНИЕ 3: Проверка аргументов на положительность
# Напиши декоратор validate_positive, который:
# - проверяет, что все переданные числовые аргументы больше 0,
# - если хотя бы один из них ≤ 0 — выбрасывает ValueError с сообщением "Все аргументы должны быть положительными".
# Пример:
# >>> @validate_positive
# >>> def multiply(a, b): return a * b
# >>> multiply(-1, 3)
# ValueError: Все аргументы должны быть положительными

from functools import wraps


def validate_positive(func):
    pass
