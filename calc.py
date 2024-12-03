def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b

def divide(a, b):
    """Возвращает частное двух чисел, если делитель не равен нулю."""
    if b == 0:
        return "Ошибка: деление на ноль невозможно."
    return a / b

def main():
    try:
        # Принимаем два числа от пользователя
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        # Выводим результаты арифметических операций
        print(f"Сложение: {num1} + {num2} = {add(num1, num2)}")
        print(f"Вычитание: {num1} - {num2} = {subtract(num1, num2)}")
        print(f"Умножение: {num1} * {num2} = {multiply(num1, num2)}")
        print(f"Деление: {num1} / {num2} = {divide(num1, num2)}")
    except ValueError:
        print("Ошибка: введите корректные числа.")

if __name__ == "__main__":
    main()
