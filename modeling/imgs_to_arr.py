import os
import subprocess

import tqdm

import numpy as np

from keras.preprocessing.image import load_img

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

img_width = int(os.environ.get("IMG_DIM"))
img_height = int(os.environ.get("IMG_DIM"))


def imgdir_to_arr(data_dir, arr_dir):
    print('Converting from: "{}"'.format(data_dir))
    print('Saving to: "{}"'.format(arr_dir))

    subprocess.call(['mkdir', '-p', arr_dir])

    cats = sorted(os.listdir(data_dir))
    cat_nbr = len(cats)
    print('Iterating over all categories')

    for cat_idx, cat in enumerate(cats):
        print('Category:', cat)
        cat_path = os.path.join(data_dir, cat)
        img_files = sorted(os.listdir(cat_path))
        for img_idx, img_file in tqdm.tqdm(enumerate(img_files)):
            img_path = os.path.join(cat_path, img_file)
            img = load_img(img_path, target_size=(img_height, img_width))
            img_name = '{}-img-{}-{}'.format(img_idx, cat, cat_idx)
            lab_name = '{}-lab-{}-{}'.format(img_idx, cat, cat_idx)
            lab = np.eye(cat_nbr, dtype=np.float32)[cat_idx]
            arr_path = os.path.join(arr_dir, img_name)
            lab_path = os.path.join(arr_dir, lab_name)
            np.save(arr_path, img)
            np.save(lab_path, lab)


if __name__ == '__main__':
    imgdir_to_arr('data/raw/train', 'data/arr/train')
    imgdir_to_arr('data/raw/test', 'data/arr/test')
