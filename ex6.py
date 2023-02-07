def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, int) and isinstance(height, int)):
        raise TypeError(
            'The width and height must be of type int.'
        )
    if not (width > 0 and height > 0):
        raise ValueError(
            'The width and height must be positive.'
        )
    return width * height


if __name__ == '__main__':
    # assert area('5','4') == 20
    assert area(5, -1) == -5