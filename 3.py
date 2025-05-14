# Початковий список чисел
numbers = [1, 2, 3, 4, 3, 2, 5, 6, 5, 7]

# Порожній список для повторюваних чисел
duplicates = []

# Проходимо по кожному числу
for num in numbers:
    # Якщо число зустрічається більше одного разу і ще не в списку duplicates
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# Виводимо результат
print("Повторювані числа:", duplicates)
