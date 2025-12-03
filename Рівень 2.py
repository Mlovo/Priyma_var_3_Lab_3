def find_substring_index(text, substring):
    len_text = len(text)
    len_sub = len(substring)

    # 1. Якщо підрядок порожній, зазвичай повертається 0 (логіка стандартного .find())
    if len_sub == 0:
        return 0

    # 2. Якщо підрядок довший за текст, знайти його неможливо
    if len_sub > len_text:
        return -1

    # 3. Зовнішній цикл
    for i in range(len_text - len_sub + 1):
        
        is_match = True  # Прапорець: припускаємо, що збіг є

        # 4. Внутрішній цикл: перевіряємо кожен символ підрядка
        for j in range(len_sub):
            if text[i + j] != substring[j]:
                is_match = False
                break

        # 5. Якщо після внутрішнього циклу прапорець все ще True, ми знайшли входження
        if is_match:
            return i

    # 6. Якщо пройшли весь цикл і не знайшли збігу
    return -1

#Перевірка
main_str = "Hello, world! Welcome to Python."
sub_str1 = "world"
sub_str2 = "Java"
sub_str3 = "Hello"
sub_str4 = "."

print(f"Текст: '{main_str}'")
print(f"Індекс '{sub_str1}': {find_substring_index(main_str, sub_str1)}") # Очікується 7
print(f"Індекс '{sub_str2}': {find_substring_index(main_str, sub_str2)}") # Очікується -1
print(f"Індекс '{sub_str3}': {find_substring_index(main_str, sub_str3)}") # Очікується 0
print(f"Індекс '{sub_str4}': {find_substring_index(main_str, sub_str4)}") # Очікується 31
