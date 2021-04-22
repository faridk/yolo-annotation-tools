import os
from random import shuffle

label_dir = ""
image_dir = ""

# Remove labels that have no images

def remove_no_image_labels():
    for path, subdirs, files in os.walk(label_dir):
        for name in files:
            image_path = os.path.join(image_dir, name[:-3] + "jpg")
            if not os.path.isfile(image_path):
                remove_path = os.path.join(path, name)
                # os.remove(remove_path)
                print(remove_path, "removed")

def remove_no_label_images():
    for path, subdirs, files in os.walk(image_dir):
        for name in files:
            label_path = os.path.join(label_dir, name[:-3] + "txt")
            if not os.path.isfile(label_path):
                remove_path = os.path.join(path, name)
                os.remove(remove_path)
                print(remove_path, "removed")

remove_no_label_images()