# 1. Создать любой метод с любым функционалом и вызвать его.
def greet(name):
    """Простой метод для приветствия."""
    return f"Привет, {name}!"

# Вызов метода
print(greet("Друг"))

# 2. Создать класс с любым набором полей и методов и вызвать их.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        """Метод для описания животного."""
        return f"{self.name}  {self.age} лет."

# Создание объекта класса Animal и вызов его методов
animal = Animal("собака1", 5)
print(animal.describe())

# 3. Создать второй класс с другим набором полей и методов, и унаследовать его от первого класса.
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        """Метод для имитации лая собаки."""
        return f"{self.name} лает!"

    def describe(self):
        """Переопределенный метод для описания собаки."""
        return f"{self.name}  {self.age} года {self.breed}."

# Создание объекта класса Dog и вызов его методов
dog = Dog("собака2", 3, "Ретривер")
print(dog.describe())  # Вызов унаследованного метода
print(dog.bark())     # Вызов нового метода
