# File Rename

import os
import exiftool
from datetime import datetime

# Path to the directory containing the files
path = os.path.abspath(os.path.join(os.path.expanduser("~"), 'projects', 'P0485 Dragon Boating Photos', '1 Raw'))

# List all files in given directory
files = os.listdir(path)

new_files = []

with exiftool.ExifToolHelper() as et:
    for file in files:
        # Get the metadata of the file
        metadata = et.get_metadata(os.path.join(path, file))[0]

        # Get the date and time the photo was taken
        date_time = metadata['Composite:SubSecCreateDate']
        timestamp = int(datetime.strptime(date_time, "%Y:%m:%d %H:%M:%S.%f%z").timestamp() * 1000)

        # Rename the file
        new_filename = f"MJVDW-{timestamp}.{file.split('.')[-1]}"
        new_files.append(new_filename)
        os.rename(os.path.join(path, file), os.path.join(path, new_filename))

        print(f'Renamed {file} to {new_filename}')

print(len(new_files), len(files))
assert len(new_files) == len(files)
