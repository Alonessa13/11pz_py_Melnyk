# Оригінальний список оцінок
grades = [85, 60, 90, 70, 55, 100, 40, 78]

# Створюємо новий список з оцінками більше 70
high_grades = [grade for grade in grades if grade > 70]

# Виводимо результат
print("Високі оцінки:", high_grades)
print("Кількість високих оцінок:", len(high_grades))
