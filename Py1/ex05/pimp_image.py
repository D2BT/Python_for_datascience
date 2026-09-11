import matplotlib.pyplot as plt

from load_image import ft_load


def ft_invert(array):
    """
    Return a copy of array with the same shape, where the
    colors are modified to invert the colors.
    Allowed operators for this function: =, +, -, * (no need to
    use them all).
    """
    result = array.copy()

    result = 255 - result

    return result


def ft_red(array):
    """
    Return a copy of array with the same shape, where the
    colors are modified to keep only the red channel.
    Allowed operators for this function: =, * (no need to
    use them all).
    """
    result = array.copy()

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            for k in range(result.shape[2]):
                if k != 0:
                    result[i][j][k] *= 0

    return result


def ft_green(array):
    """
    Return a copy of array with the same shape, where the
    colors are modified to keep only the green channel.
    Allowed operators for this function: =, - (no need to
    use them all).
    """
    result = array.copy()

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            for k in range(result.shape[2]):
                if k != 1:
                    result[i][j][k] -= result[i][j][k]

    return result


def ft_blue(array):
    """
    Return a copy of array with the same shape, where the
    colors are modified to keep only the blue channel.
    Allowed operators for this function: = (no need to
    use them all).
    """
    result = array.copy()

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            for k in range(result.shape[2]):
                if k != 2:
                    result[i][j][k] = 0

    return result


def ft_grey(array):
    """
    Return a copy of array with the same shape, where the
    colors are modified to convert to greyscale.
    Allowed operators for this function: =, / (no need to
    use them all).
    """
    result = array.copy()

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i][j] = result[i][j].sum() / 3

    return result


def main():
    """
    Load landscape.jpg, apply ft_invert / ft_red / ft_green /
    ft_blue / ft_grey to it, display each result, and print
    ft_invert.__doc__ as the subject's example does.
    """
    array = ft_load("landscape.jpg")

    inverted = ft_invert(array)
    red = ft_red(array)
    green = ft_green(array)
    blue = ft_blue(array)
    grey = ft_grey(array)

    print(ft_invert.__doc__)

    plt.imshow(inverted)
    plt.show()

    plt.imshow(red)
    plt.show()

    plt.imshow(green)
    plt.show()

    plt.imshow(blue)
    plt.show()

    plt.imshow(grey)
    plt.show()


if __name__ == "__main__":
    main()
