import os
from random import shuffle

dir = ""
list_file = open("", "w")
file_paths = []

for path, subdirs, files in os.walk(dir):
    for name in files:
        img_path = path[:-6] + "images"
        file_path = os.path.join(img_path, name)
        file_paths.append(file_path)

shuffle(file_paths)

for file_path in file_paths:
    # file_path = os.path.join(path, name)
    list_file.write(file_path[:-4] + ".jpg\n")