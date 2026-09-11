from PIL import Image
import numpy as np


def ft_load(path: str):
    """
    Load the image at path and return its pixel content as a numpy
    array in RGB format. Prints the shape of the image. Works for
    any format Pillow can decode, including JPG/JPEG. Handles any
    error (missing file, invalid path, unreadable image...) with a
    clear message instead of crashing.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        img = Image.open(path)
        array = np.array(img.convert("RGB"))
        print(f"The shape of image is: {array.shape}")
        return array
    except (OSError, TypeError) as e:
        print(f"ft_load: error: {e}")
        return None


def main():
    """Call ft_load on an example image and print the result."""
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
