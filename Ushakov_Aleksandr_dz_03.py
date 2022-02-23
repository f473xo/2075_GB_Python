import os
import shutil


project = "my_project"
try:
    for folder, directory, files in os.walk(project):
        if 'templates' in directory and folder != project:
            for i in os.listdir(os.path.join(folder, 'templates')):
                shutil.copytree(os.path.join(folder, 'templates', i), os.path.join(project, 'templates', os.path.basename(folder)))
except FileExistsError:
    print("Сбор уже завершен.")
