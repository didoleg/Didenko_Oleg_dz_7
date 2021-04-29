import os

create_folders = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for key, val in create_folders.items():
    if os.path.exists(key):
        for folder in val:
            path = os.path.join(os.getcwd(), key, folder)
            if os.path.exists(path) is not True:
                os.mkdir(path)
    else:
        os.mkdir(key)
        for folder in val:
            os.mkdir(os.path.join(os.getcwd(), key, folder))
