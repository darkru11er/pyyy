import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random

# Функции для арифметических операций
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль невозможно."
    return a / b

# Функция для выполнения арифметической операции
def perform_arithmetic_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа.")
        return

    operation = operation_var.get()

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
        if isinstance(result, str):  # Проверка на ошибку деления на ноль
            messagebox.showerror("Ошибка", result)
            return
    else:
        messagebox.showerror("Ошибка", "Выберите операцию.")
        return

    result_label.config(text=f"Результат: {result}")

# Функции для работы с файлами
def generate_and_write_numbers():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    try:
        count = int(entry_count.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное количество чисел.")
        return

    numbers = [random.randint(1, 100) for _ in range(count)]
    with open(file_path, 'w') as file:
        file.write("\n".join(map(str, numbers)))

    messagebox.showinfo("Успех", f"Числа записаны в файл: {file_path}")

def read_and_calculate():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при чтении файла: {e}")
        return

    if not numbers:
        messagebox.showerror("Ошибка", "Файл пуст или содержит некорректные данные.")
        return

    average = sum(numbers) / len(numbers)
    messagebox.showinfo("Результат", f"Среднее значение: {average}")

# Создание основного окна
root = tk.Tk()
root.title("Многозадачная программа")

# Создание вкладок
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# Вкладка для арифметических операций
arithmetic_frame = ttk.Frame(notebook)
notebook.add(arithmetic_frame, text="Арифметика")

tk.Label(arithmetic_frame, text="Введите первое число:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(arithmetic_frame)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(arithmetic_frame, text="Введите второе число:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(arithmetic_frame)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(arithmetic_frame, text="Выберите операцию:").grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar(value="add")
tk.Radiobutton(arithmetic_frame, text="Сложение", variable=operation_var, value="add").grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
tk.Radiobutton(arithmetic_frame, text="Вычитание", variable=operation_var, value="subtract").grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)
tk.Radiobutton(arithmetic_frame, text="Умножение", variable=operation_var, value="multiply").grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)
tk.Radiobutton(arithmetic_frame, text="Деление", variable=operation_var, value="divide").grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)

calculate_button = tk.Button(arithmetic_frame, text="Вычислить", command=perform_arithmetic_operation)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

result_label = tk.Label(arithmetic_frame, text="Результат: ")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Вкладка для работы с файлами
file_frame = ttk.Frame(notebook)
notebook.add(file_frame, text="Работа с файлами")

tk.Label(file_frame, text="Введите количество чисел:").grid(row=0, column=0, padx=10, pady=10)
entry_count = tk.Entry(file_frame)
entry_count.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(file_frame, text="Сгенерировать и записать числа", command=generate_and_write_numbers)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

read_button = tk.Button(file_frame, text="Прочитать и вычислить среднее", command=read_and_calculate)
read_button.grid(row=2, column=0, columnspan=2, pady=10)

# Запуск основного цикла событий
root.mainloop()
