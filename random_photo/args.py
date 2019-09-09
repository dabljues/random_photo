import argparse
import os


def handle_command_line_arguments() -> argparse.Namespace:
    """Handle script's command line arguments.

    Returns:
        argparse.Namespace: script's command line arguments
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('photos_dir', type=str)
    parser.add_argument(
        '--used_photos',
        '-u',
        type=str,
        default='used_photos.txt')
    arguments: argparse.Namespace = parser.parse_args()
    arguments.photos_dir = os.path.abspath(arguments.photos_dir)
    return arguments
