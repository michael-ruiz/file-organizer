import os
import shutil
import sys

# Path to directory
dir = sys.argv[1]

# Create new folders for organizing
new_folders = {'p':'pdf-files', 'w':'word-files', 'pn':'png-files', 'm':'misc'}
for key, folder in new_folders.items():
    f = os.path.join(dir, folder)
    if not os.path.exists(f):
        os.mkdir(f)

for filename in os.listdir(dir):
    if filename.endswith('.pdf'):
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders['p'], filename)
        shutil.move(old_dir, new_dir)
    elif filename.endswith('.docx'):
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders['w'], filename)
        shutil.move(old_dir, new_dir)
    elif filename.endswith('.png'):
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders['pn'], filename)
        shutil.move(old_dir, new_dir)
    else:
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders['m'], filename)
        shutil.move(old_dir, new_dir)
