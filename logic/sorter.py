import os
from PIL import Image

from PIL import Image
from PIL.ExifTags import TAGS


def get_date(path):
    try:
        with Image.open(path) as img:
            exif_data = img.getexif()
            if not exif_data:
                return None

            # name mapping
            tags = {TAGS.get(tag_id, tag_id): value for tag_id, value in exif_data.items()}

            exif_ifd = exif_data.get_ifd(0x8769)

            if exif_ifd:
                tags.update({TAGS.get(tag_id, tag_id): value for tag_id, value in exif_ifd.items()})

            # setting priorities
            priorities = ['DateTimeOriginal', 'DateTaken', 'DateTime', 'DateTimeDigitized']

            for tag in priorities:
                if tag in tags:
                    print(f"Found through: {tag}")
                    return tags[tag]

    except Exception as e:
        print(f"Error occurred {path}: {e}")

    return None


def move_photo(source_path, date_str, base_destination):
    if not date_str:
        # creating folder for photos without creation date
        target_dir = os.path.join(base_destination, "Unknown")

    else:
        # getting year and month from date
        year = date_str.split(":")[0]
        month = date_str.split(":")[1]

        # creating folder (e.g. ./output/2023/10)
        target_dir = os.path.join(base_destination, year, month)

    # create folder if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # defining final destination
    file_name = os.path.basename(source_path)
    name, ext = os.path.splitext(file_name)
    final_path = os.path.join(target_dir, file_name)

    counter = 1

    # handling duplicit files
    while os.path.exists(final_path):
        new_name = f"{name}_{counter}{ext}"
        final_path = os.path.join(target_dir, new_name)
        counter += 1

    try:
        os.replace(source_path, final_path)
        print(f"Moved: {os.path.basename(final_path)} -> {target_dir}")
    except FileNotFoundError:
        print("Source file not found")
    except Exception as e:
        print(f"An error occurred: {e}")