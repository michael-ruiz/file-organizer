import os
import shutil

# Path to directory
dir = 'test-file'

# Create new folders for organizing
new_folders = ['pdf-files', 'word-files', 'png-files', 'misc']
for folder in new_folders:
    f = os.path.join(dir, folder)
    if not os.path.exists(f):
        os.mkdir(f)

for filename in os.listdir(dir):
    if filename.endswith('.txt'):
        old_dir = os.path.join(dir, filename)
        new_dir = os.path.join(dir, new_folders[3], filename)
        shutil.move(old_dir, new_dir)
