def num_translate_adv(value):
    """Переводит числительное с английского на русский"""
    values = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    return values.get(value)


print(num_translate_adv('one'))
print(num_translate_adv('eight'))
print(num_translate_adv('Twenty'))
