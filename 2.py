# Список покупок
products = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]

# Створюємо новий список з назвами довшими за 4 символи
long_products = [item for item in products if len(item) > 4]

# Виводимо результат
print("Товари з довгою назвою:", long_products)
print("Кількість таких товарів:", len(long_products))
