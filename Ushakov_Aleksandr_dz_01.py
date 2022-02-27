import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную mail-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого eemail
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    re_mail = re.compile(r'\w*[@]\w*[\.]\w*')
    data, data1 = re_mail.match(email).group(0).split('@')
    if not re_mail.match(email):
        raise ValueError(f'Неправильный адрес электронной почты: {email}')
    return {'username': data, 'domain': data1}


for el in ['someone@geekbrains.com', 'someone@geekbrainscom']:
    try:
        print(email_parse(el))
    except AttributeError:
        print(f'Проверьте правильно ли введен адрес - {el}')
