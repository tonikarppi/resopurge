"""
This script is used for removing image files that have a lower width/height than
the specified values.
"""

import os
from getpass import getuser
from PIL import Image

# The path to your images.
IMAGES_PATH = f"/home/{getuser()}/Pictures/wallpapers"

# Minimum image dimensions.
MIN_WIDTH = 1920
MIN_HEIGHT = 1080


def get_files_recursively(root_path):
    files_in_paths = [(root, files) for root, dirs, files in os.walk(root_path)]
    return [
        f"{path}/{file}"
        for path, files in files_in_paths
        for file in files
        if file.lower().endswith((".png", ".jpg"))
    ]


def image_smaller_than(image_path, width, height):
    image = Image.open(image_path)
    return image.width < width or image.height < height


def delete_files(files):
    for file in files:
        os.remove(file)


def main():
    image_files = get_files_recursively(IMAGES_PATH)
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
