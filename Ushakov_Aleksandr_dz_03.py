tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Александр', 'Павел']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    result = None
    for el in range(len(tutors)):
        if len(klasses) < len(tutors) and el >= len(klasses):
            yield tutors[el], result
        else:
            yield tutors[el], klasses[el]


generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
