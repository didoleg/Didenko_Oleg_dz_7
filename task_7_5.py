import os
import json

file_size_dict = {}
all_files = []

for root, dirs, files in os.walk('./'):
    for file in files:
        path_file = os.path.join(root, file)
        mask_file = os.path.join(root, file).split('.')[-1]
        all_files.append((os.stat(path_file).st_size, mask_file))

key_size_max, _ = max(all_files)
for file_size in range(len(str(key_size_max)) - 1):
    key_size = 100 * 10 ** file_size
    file_size_dict.setdefault(key_size, (0, []))

for file in all_files:
    if len(str(file[0])) < 2:
        count, type_file = file_size_dict[(10 * 10 ** len(str(file[0])))]
        type_file.append(file[1])
        type_file = list(set(type_file))
        file_size_dict[(10 * 10 ** len(str(file[0])))] = (count + 1, type_file)
    else:
        count, type_file = file_size_dict[(10 ** len(str(file[0])))]
        type_file.append(file[1])
        type_file = list(set(type_file))
        file_size_dict[(10 ** len(str(file[0])))] = (count + 1, type_file)

with open('file_size_dict.json', 'w') as f:
    json.dump(file_size_dict, f)
