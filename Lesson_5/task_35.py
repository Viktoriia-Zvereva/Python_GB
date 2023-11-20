"""Даны два целых числа A и В. 
Выведите все числа от A до B включительно, в порядке возрастания, 
если A < B, или в порядке убывания, если A > B"""



def print_numbers(a, b):
    if a == b:  # Выход из рекурсии - без этого условия программа зависнет
        return f"{a}"
    if a > b:
        # Вычетаем 1, так как печатаем по убыванию
        return f"{a}, {print_numbers(a - 1, b)}"
    if a < b:
        # Добавляем 1, так как печатаем по возрастанию
        return f"{a}, {print_numbers(a + 1, b)}"


print(print_numbers(1, 3))
print(print_numbers(5, 1))
