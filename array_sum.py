def sum_negative_between_min_max(arr):
    """
    Находит сумму отрицательных элементов, расположенных
    между максимальным и минимальным элементами массива.
    
    Args:
        arr: список чисел (int или float)
    
    Returns:
        Сумма отрицательных элементов между min и max.
        Если между min и max нет отрицательных элементов — возвращает 0.
    
    Raises:
        ValueError: если массив пустой или содержит нечисловые значения.
    """
    if not arr:
        raise ValueError("Массив не должен быть пустым")
    
    # Находим индексы максимума и минимума
    max_idx = arr.index(max(arr))
    min_idx = arr.index(min(arr))
    
    # Определяем границы диапазона (между = строго между, не включая сами min/max)
    left = min(max_idx, min_idx) + 1
    right = max(max_idx, min_idx)
    
    # Суммируем отрицательные элементы в диапазоне
    total = sum(x for x in arr[left:right] if x < 0)
    
    return total