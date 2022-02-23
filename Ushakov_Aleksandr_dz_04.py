import os
import django
import collections


def collecting_info():
    origin_directory = django.__path__[0]
    files_list = collections.defaultdict(int)
    for folder, directory, files in os.walk(origin_directory):
        for el in files:
            size = 10 ** len(str(os.stat(os.path.join(folder, el)).st_size))
            files_list[size] += 1
    for size, nums in sorted(files_list.items()):
        print(f'{size}:{nums}')


collecting_info()
