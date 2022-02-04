#def convert_time(duration: int) -> str:
duration = int(input('Введите целое число в секундах: '))
if duration > 0 and duration < 60:
    print((duration), 'сек')
elif duration >= 60 and duration < 3600:
    print((duration // 60), 'мин', (duration % 60), 'сек')
elif duration >= 3600 and duration < 86400:
    print((duration // 3600), 'час', (duration % 3600 // 60), 'мин', (duration % 3600 % 60), 'сек')
elif duration >= 86400 and duration < 31556926:
    print((duration // 86400), 'дн', (duration % 86400 // 3600), 'час', (duration % 86400 % 3600 // 60), 'мин', (duration % 86400 % 3600 % 60), 'сек')
else:
    duration >= 31556926
    print('Ваше число больше года, я не справляюсь :(')