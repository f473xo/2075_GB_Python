import os


name_list = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}
for key, value in name_list.items():
    if not os.path.exists(key):
        for item in value:
            for i in item.keys():
                os.makedirs(os.path.join(key, i))
