def greet(name):
    """
    Функция для приветствия пользователя.

    Args:
        name (str): Имя пользователя.

    Returns:
        str: Приветственное сообщение.
    """
    return f"Привет, {name}!"

def main():
    # Ввод имени пользователя
    name = input("Введите ваше имя: ")

    # Приветствие пользователя
    greeting = greet(name)

    # Вывод приветствия в консоль
    print(greeting)

    # Вывод текста в любом месте (например, в файл)
    with open("greeting.txt", "w") as file:
        file.write(greeting)

if __name__ == "__main__":
    main()
