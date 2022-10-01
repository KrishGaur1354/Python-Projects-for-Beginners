import os
import shutil

ld = os.listdir()

for file in ld:
    if not '.' in file or os.path.isdir(file):
        continue
    else:
        if file == os.path.basename(__file__):
            continue
        ext = file.split('.')[-1]
        directory = ext.upper()+'s'
        
        if directory in ld:
            print(f'Skipping {directory} directory...')
        else:
            print(f'Creating {directory} directory...')
            os.mkdir(directory)
            ld.append(directory)
        
        try:
            shutil.move(file, directory)
            print(f'File {file} moved successfully!\n')
        except shutil.Error as e:
            print(e)
            continue