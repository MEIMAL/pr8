while True:
    try:
        # Запрашиваем у пользователя два целых числа
        n1 = int(input("Введите первое целое число: "))
        n2 = int(input("Введите второе целое число: "))
        # Вычисляем сумму
        result = n1 + n2
        # Выводим результат
        print(f"Сумма {n1} и {n2} равна {result}")
    except ValueError:
        print("Введите корректные целые числа.")
