import os.path
from sys import argv
from PIL import Image


def search_directory(directory):
    """Searches for matching directory based on input parameter."""
    search_dir = ""
    for root, dirs, files in os.walk(os.getcwd(), topdown=True):
        for name in dirs:
            if name == directory:
                search_dir = os.path.join(root, name)
    return os.listdir(search_dir)


def convert(input_file, path, directory):
    """Converts incoming image file, to have the PNG format, and saves converted imagine to location of choice."""
    name = input_file.split(".")[0]
    img = Image.open(f"{directory}/{input_file}")
    img.save(f"{path}{name}.png", "png")
    return


if __name__ == "__main__":
    # Takes directory to search and name of new directory to create, as input from the terminal.
    searched = argv[1]
    dir_to_create = argv[2]
    files_to_convert = search_directory(searched)

    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)

    for file in files_to_convert:
        convert(file, dir_to_create, searched)
