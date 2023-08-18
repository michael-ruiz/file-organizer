import os
import shutil
import sys

# Path to directory
dir = sys.argv[1]

# Create new folders for organizing
new_folders = {'p':'pdf-files', 'w':'word-files', 'img':'image-files', 't':'text-files'}
for key, folder in new_folders.items():
    f = os.path.join(dir, folder)
    if not os.path.exists(f):
        os.mkdir(f)

# Move files
for filename in os.listdir(dir):
    if filename.endswith('.pdf'):
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders['p'], filename)
        shutil.move(old_dir, new_dir)
    if filename.endswith('.docx') or filename.endswith('.doc'):
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders['w'], filename)
        shutil.move(old_dir, new_dir)
    if filename.endswith('.txt'):
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders['t'], filename)
        shutil.move(old_dir, new_dir)
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders['img'], filename)
        shutil.move(old_dir, new_dir)
