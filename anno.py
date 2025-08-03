import os

file = './training/Oracle-P15K/train.json'
f = open(file, 'w')

root = '/path/to/training/set'
for mode in os.listdir(root):
    mode_path = os.path.join(root, mode)
    for img in os.listdir(mode_path):
        f.write(
            '{{"source": "input/{}", "target": "target/{}", "prompt": ""}}\n'.format(img, img))
    break
