from array_sum import sum_negative_between_min_max


def main():
    # Пример 1: базовый тест
    arr1 = [3, -2, 7, -5, 1, -8, 4, -1, 6]
    # max = 7 (индекс 2), min = -8 (индекс 5)
    # между ними: -5, 1  →  отрицательных: -5  →  сумма = -5
    print(f"Массив: {arr1}")
    print(f"Сумма отрицательных между max и min: {sum_negative_between_min_max(arr1)}\n")
    
    # Пример 2: пользовательский ввод
    try:
        n = int(input("Введите размерность N: "))
        arr = []
        for i in range(n):
            arr.append(float(input(f"A[{i}] = ")))
        
        result = sum_negative_between_min_max(arr)
        print(f"\nРезультат: {result}")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    main()