import os
import shutil

path = os.path.join(os.getcwd(), 'my_project')
for root, dirs, files in os.walk(path):
    for file in files:
        if file.lower().endswith('.html'):
            file_path = os.path.join(root, file)

            if os.path.exists(os.path.join(path, 'templates')) is not True:
                os.makedirs(os.path.join(path, 'templates', os.path.basename(root)))

            copy_path = (os.path.join(path, 'templates', os.path.basename(root)))

            if os.path.exists(copy_path) is not True:
                os.mkdir(copy_path)

            if os.path.exists(os.path.join(copy_path, file)) is not True:
                shutil.copy(file_path, copy_path)
