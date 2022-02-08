from random import choice

nouns = ['автомобиль', 'лес', 'огонь','город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjektives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']


def get_jokes(count: int) -> list:
    """Возвращает список шуток в кол-ве count зарандомив их из предложенных списков"""
    for elem in range(count):
        list_out = (f'{choice(nouns)} {choice(adverbs)} {choice(adjektives)}')
    return list_out


print(get_jokes(2))
print(get_jokes(10))