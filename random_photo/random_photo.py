"""Main application module."""
import argparse
import os
import random
import sys
from typing import List, Set

from args import handle_command_line_arguments
from file_utils import photo_valid, read_used_photos_file
from photo import Photo


def random_photo() -> int:
    arguments: argparse.Namespace = handle_command_line_arguments()

    used_photos: Set[str] = read_used_photos_file(arguments.used_photos)
    photos: List[Photo] = [
        Photo(
            arguments.photos_dir,
            photo_path) for photo_path in os.listdir(
                arguments.photos_dir) if photo_valid(photo_path, used_photos)]
    selected_photo: Photo = random.choice(photos)
    print(selected_photo)


if __name__ == '__main__':
    random_photo()
