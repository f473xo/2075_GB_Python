import itertools
import json

with open('hobby.csv', 'r', encoding='utf-8') as w:
    hobby = [i.rstrip() for i in w]
    with open('users.csv', 'r', encoding='utf-8') as a:
        users = [i.rstrip().replace(',', ' ') for i in a]
        if len(users) >= len(hobby):
            with open('task_6_3_result.json', 'w', encoding='utf-8') as s:
                d = (itertools.zip_longest(users, hobby))
                users_hobby = {str(i[0]).strip(): str(i[1]).strip() for i in d}
                print(users_hobby)
                json.dump(users_hobby, s, ensure_ascii=False, indent=4)
        else:
            exit(1)
