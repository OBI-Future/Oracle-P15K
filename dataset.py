import json
import os
import random

import cv2
import numpy as np
from torch.utils.data import Dataset


def data_augmentation(image, mode):
    if mode == 0:
        # original
        out = image
    elif mode == 1:
        # flip up and down
        out = np.flipud(image)
    elif mode == 2:
        # rotate counterwise 90 degree
        out = np.rot90(image)
    elif mode == 3:
        # rotate 90 degree and flip up and down
        out = np.rot90(image)
        out = np.flipud(out)
    elif mode == 4:
        # rotate 180 degree
        out = np.rot90(image, k=2)
    elif mode == 5:
        # rotate 180 degree and flip
        out = np.rot90(image, k=2)
        out = np.flipud(out)
    elif mode == 6:
        # rotate 270 degree
        out = np.rot90(image, k=3)
    elif mode == 7:
        # rotate 270 degree and flip
        out = np.rot90(image, k=3)
        out = np.flipud(out)
    else:
        raise Exception('Invalid choice of image transformation')

    return out


def random_augmentation(*args):
    out = []
    flag_aug = random.randint(0, 7)
    for data in args:
        out.append(data_augmentation(data, flag_aug).copy())
    out.append(flag_aug)
    return out


def bounding_box(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _, binary_image = cv2.threshold(
        image_gray, 128, 255, cv2.THRESH_BINARY)

    white_points = cv2.findNonZero(binary_image)

    x, y, w, h = cv2.boundingRect(white_points)

    return x, y, w, h


class MyDataset(Dataset):
    def __init__(self, prompt_file, data_root):
        self.data = []
        self.prompt_file = prompt_file
        self.data_root = data_root
        with open(self.prompt_file, 'rt') as f:
            for line in f:
                self.data.append(json.loads(line))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        source_filename = item['source']
        target_filename = item['target']
        prompt = item['prompt']

        source = cv2.imread(self.data_root + source_filename)
        target = cv2.imread(self.data_root + target_filename)
        style = cv2.imread(self.data_root + target_filename)

        # Do not forget that OpenCV read images in BGR order.
        try:
            source = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
        except:
            print(self.data_root + source_filename)
            raise
        target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)
        style = cv2.cvtColor(style, cv2.COLOR_BGR2RGB)

        x, y, w, h = bounding_box(source)
        style[y:y + h, x:x + w] = 0

        # source, target, style, mode = random_augmentation(
        #     source, target, style)

        # Normalize source images to [0, 1].
        source = source.astype(np.float32) / 255.0

        # Normalize target images to [-1, 1].
        target = (target.astype(np.float32) / 127.5) - 1.0

        name = source_filename.split(
            '.')[0] + '_' + os.path.basename(target_filename)
        return dict(jpg=target, txt=prompt, hint=source, style=style, name=name)
