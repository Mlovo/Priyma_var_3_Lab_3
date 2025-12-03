def number_to_ukrainian_text(n):
    if not (0 <= n <= 10000):
        return "Число має бути від 0 до 10000"

    # Словники для частин числа
    units = ["", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять"]
    teens = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", 
             "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев'ятнадцять"]
    tens = ["", "", "двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", 
            "сімдесят", "вісімдесят", "дев'яносто"]
    hundreds = ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", 
                "сімсот", "вісімсот", "дев'ятсот"]

    # 1. Базові випадки
    if n == 0:
        return "нуль"
    if n == 10000:
        return "десять тисяч"

    parts = []

    # 2. Обробка тисяч
    thou = n // 1000
    remainder = n % 1000

    if thou > 0:
        if thou == 1:
            parts.append("одна тисяча")
        elif thou == 2:
            parts.append("дві тисячі")
        elif thou in [3, 4]:
            parts.append(units[thou] + " тисячі")
        else:
            parts.append(units[thou] + " тисяч")

    # 3. Обробка залишку (сотні, десятки, одиниці)
    if remainder > 0:
        h = remainder // 100        
        t_rem = remainder % 100   


        if h > 0:
            parts.append(hundreds[h])

        if t_rem > 0:
            if t_rem < 10:
                parts.append(units[t_rem])
            elif 10 <= t_rem < 20:
                parts.append(teens[t_rem - 10])
            else:
                t = t_rem // 10 # Десятки
                u = t_rem % 10  # Одиниці
                parts.append(tens[t])
                if u > 0:
                    parts.append(units[u])

    return " ".join(parts)


try:
    test_number = int(input("Введіть число від 0 до 10000: "))
except ValueError:
    print("Введіть, будь ласка, ціле число.")
else:
    if 0 <= test_number <= 10000:
        print(f"{test_number}: {number_to_ukrainian_text(test_number)}")
    else:
        print("Число має бути від 0 до 10000")
