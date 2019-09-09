import os
from dataclasses import dataclass


@dataclass
class Photo:
    path: str
    file_name: str

    def __init__(self, photos_dir, photo_path):
        self.path = os.path.join(photos_dir, photo_path)
        self.file_name = os.path.basename(self.path)
