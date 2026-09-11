import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def ft_transpose(array):
    """
    Return array transposed by hand (swap rows and columns
    yourself, e.g. with loops/indexing). No transpose method
    or library function is allowed for this.
    """
    nouveau = [
        [0 for row in range(len(array))]
        for col in range(len(array[0]))
        ]

    for i in range(len(array)):
        for j in range(len(array[i])):
            nouveau[j][i] = array[i][j]

    return nouveau


def main():
    """
    Load animal.jpeg, cut a square part of it, transpose it by hand
    with ft_transpose, display it, and print the new shape and the
    data of the image after the transpose.
    """
    # quick sanity check on ft_transpose with a small array you
    # can verify by hand: [[1, 2, 3], [4, 5, 6]] transposed should
    # be [[1, 4], [2, 5], [3, 6]]
    small = [[1, 2, 3], [4, 5, 6]]
    print(ft_transpose(small))

    array = ft_load("animal.jpeg")
    print(array)

    square = array[100:500, 300:700]
    print(f"New shape after slicing: {square.shape}")

    transposed = np.array(ft_transpose(square))
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    plt.imshow(transposed)
    plt.show()


if __name__ == "__main__":
    main()
