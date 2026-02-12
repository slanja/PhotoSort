import os
import sys

from logic.sorter import get_date, move_photo

def run_sorting(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # get date
        date = get_date(file_path)

        # move photo to it's folder
        move_photo(file_path, date, destination_folder)