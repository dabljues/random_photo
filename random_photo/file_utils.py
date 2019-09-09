import os
from typing import List, Set

from photo import Photo


def read_used_photos_file(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as used_photos_file:
            return set(line.strip() for line in used_photos_file.readlines())
    except FileNotFoundError:
        return set()


def add_photo_to_used_photos_file(selected_photo: Photo) -> None:
    raise NotImplementedError


def photo_already_used(photo_path: str, used_photos: Set[str]) -> bool:
    return photo_path in used_photos


def photo_valid(photo_path: str, used_photos: Set[str]) -> bool:
    return not (os.path.isdir(photo_path) or
                photo_already_used(photo_path, used_photos))
