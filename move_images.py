import re
import os

BASE_DIR = '../archive/tiny-imagenet-200/val/'

with open(f'{BASE_DIR}/val_annotations.txt') as f:
    lines = f.readlines()

    for line in lines:
        [image, folder, *rest] = re.split(r'\s+', line)

        class_folder = os.path.join(BASE_DIR, 'images', folder)
        if not os.path.exists(class_folder):
            os.mkdir(class_folder)

        img_path = os.path.join(BASE_DIR, 'images', image)

        if os.path.exists(img_path):
            os.rename(img_path, os.path.join(class_folder, image))