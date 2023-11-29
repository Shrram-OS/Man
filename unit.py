import cl4py

class MyClass:
    def __init__(self):
        # Инициализация объекта lisp при создании экземпляра класса
        self.lisp = cl4py.Lisp()

    def eval(self, some_variable):
        # Выполнение выражения Lisp с использованием переданной переменной
        return self.lisp.eval(some_variable)

# Пример использования
my_instance = MyClass()

# Передаем выражение Lisp для вычисления
result = my_instance.eval("('+', 1, 2)")

# Вывод результата
print(result)
