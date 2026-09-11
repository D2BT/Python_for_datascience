import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def ft_zoom(
    array: np.ndarray,
    y_start: int,
    y_end: int,
    x_start: int,
    x_end: int,
) -> np.ndarray:
    """
    Return a cropped ("zoomed") version of array, keeping only the
    rows between y_start and y_end, and the columns between x_start
    and x_end (use slicing on both axes, not a manual loop). Only
    the first color channel is kept, so the result looks greyscale.
    """
    return array[y_start:y_end, x_start:x_end, 0:1]


def main():
    """
    Load animal.jpeg, print its size (X, Y), its number of
    channels, and its pixel content. Then slice/zoom into a
    part of the image (using slicing) and display it with the
    scale shown on both axes. Handle any error with a clear
    message, without crashing.
    """
    array = ft_load("animal.jpeg")
    print(array)

    zoomed = ft_zoom(array, 100, 500, 300, 700)
    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)

    plt.imshow(zoomed, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
