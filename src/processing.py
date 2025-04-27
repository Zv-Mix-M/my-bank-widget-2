# src/processing.py
"""
Модуль processing для фильтрации и сортировки банковских операций.

Функции:
- filter_by_state
- sort_by_date
"""

from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]],
    state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Возвращает список словарей (операций), в которых значение по ключу 'state'
    совпадает с указанным параметром state.

    :param operations: Список операций (каждая операция — словарь с ключами 'id', 'state', 'date', etc.).
    :param state: Статус операции, по умолчанию 'EXECUTED'.
    :return: Новый список отфильтрованных операций по переданному статусу.
    """
    filtered_operations = []
    for op in operations:
        if op.get('state') == state:
            filtered_operations.append(op)
    return filtered_operations


def sort_by_date(
    operations: List[Dict[str, Any]],
    reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Возвращает новый список операций, отсортированный по дате (ключ 'date').

    :param operations: Список операций (каждая операция — словарь с ключом 'date').
    :param reverse: Порядок сортировки; по умолчанию True (убывающая сортировка).
    :return: Список операций, отсортированный по дате.
    """
    # Предполагаем, что дата в формате "2019-07-03T18:35:29.512364"
    # Сортируем с использованием datetime.strptime
    return sorted(
        operations,
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse
    )
