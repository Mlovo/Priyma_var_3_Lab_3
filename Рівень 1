def is_natural_recursive(n):
    # 1. Перевірка типу: натуральні числа повинні бути цілими (int)
    if not isinstance(n, int):
        return False
    
    if n == 1:
        return True
    
    if n < 1:
        return False
    
    # 2. Рекурсивний крок: зменшуємо число на 1 і перевіряємо знову
    return is_natural_recursive(n - 1)

# Тестування функції з різними вхідними даними
test_numbers = [5, 1, 0, -5, 2.5, "3", 10]

print(f"{'Число':<10} | {'Результат'}")
print("-" * 25)

for num in test_numbers:
    try:
        result = is_natural_recursive(num)
        print(f"{str(num):<10} | {result}")
    except RecursionError:
        print(f"{str(num):<10} | Помилка (занадто велике число)")
