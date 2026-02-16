import os
import datetime
from PIL import Image
from PIL.ExifTags import TAGS


def get_all_exif(path):
    try:
        with Image.open(path) as img:
            exif_data = img.getexif()
            if not exif_data:
                return {}

            # getting readable exif (e. g. 36867 -> 'DateTimeOriginal')
            readable_exif = {TAGS.get(tag_id, tag_id): value for tag_id, value in exif_data.items()}

            # getting more exif data
            exif_ifd = exif_data.get_ifd(0x8769)
            if exif_ifd:
                readable_exif.update({TAGS.get(tag_id, tag_id): value for tag_id, value in exif_ifd.items()})

            return readable_exif
    except Exception:
        return {}


def get_date(path):
    # getting exif from photo/video
    exif_dict = get_all_exif(path)

    # defining priorities
    priorities = ['DateTimeOriginal', 'DateTimeDigitized', 'DateTime']

    for key in priorities:
        value = exif_dict.get(key)

        # checking if date isn't empty or null
        if value and isinstance(value, str) and not value.startswith("0000"):
            return value

    # fallback: modification date
    ts = os.path.getmtime(path)
    return datetime.datetime.fromtimestamp(ts).strftime('%Y:%m')


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