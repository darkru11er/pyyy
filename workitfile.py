import random

def generate_and_write_numbers(file_path, count=10, lower_bound=1, upper_bound=100):
    """Генерирует случайные числа и записывает их в файл."""
    numbers = [random.randint(lower_bound, upper_bound) for _ in range(count)]
    with open(file_path, 'w') as file:
        file.write("\n".join(map(str, numbers)))
    return numbers

def read_and_calculate(file_path):
    """Читает числа из файла и вычисляет их среднее значение."""
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    average = sum(numbers) / len(numbers)
    return numbers, average

def main():
    # Пользователь выбирает файл для записи и чтения
    file_path = input("Введите путь к файлу для записи и чтения: ")

    # Генерация и запись случайных чисел в файл
    numbers = generate_and_write_numbers(file_path)
    print(f"Сгенерированные числа: {numbers}")

    # Чтение чисел из файла и вычисление среднего значения
    read_numbers, average = read_and_calculate(file_path)
    print(f"Содержимое файла: {read_numbers}")
    print(f"Среднее значение: {average}")

if __name__ == "__main__":
    main()
