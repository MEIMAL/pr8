while True:
    try:
        # Ввод двух чисел
        a = int(input("Введите первое число (a): "))
        b = int(input("Введите второе число (b): "))
        break  # Выход из цикла, если ввод корректен
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целые числа.")
# Определение границ
start = min(a, b) + 1
end = max(a, b)
# Вывод целых чисел между a и b
print(f"Целые числа между {a} и {b}:")
for i in range(start, end):
    print(i)
