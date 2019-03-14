"""
This script is used for removing image files that have a lower width/height than
the specified values.
"""

import os
from getpass import getuser
from os.path import join
from pathlib import Path

from PIL import Image

# The path to your images.
IMAGES_PATH = f"/home/{getuser()}/Pictures/wallpapers"

# Minimum image dimensions.
MIN_WIDTH = 1920
MIN_HEIGHT = 1080


def get_files_recursively(root_path):
    for current_path, dir_names, file_names in os.walk(root_path):
        for file_name in file_names:
            yield join(current_path, file_name)


def file_has_extension(file_path, *extensions):
    path = Path(file_path)
    return path.suffix.lower() in extensions


def image_smaller_than(image_path, width, height):
    image = Image.open(image_path)
    return image.width < width or image.height < height


def delete_files(files):
    for file in files:
        os.remove(file)


def main():
    files = get_files_recursively(IMAGES_PATH)
    image_files = (file for file in files if file_has_extension(file, ".jpg", ".png"))
    small_images = [
        image
        for image in image_files
        if image_smaller_than(image, MIN_WIDTH, MIN_HEIGHT)
    ]

    answer = input(
        f"You are about to remove {len(small_images)} files. Continue? y/[n]\n"
    )

    if answer.lower() != "y":
        print("Aborting.")
        return

    delete_files(small_images)
    print(f"Removed {len(small_images)} files.")


if __name__ == "__main__":
    main()
