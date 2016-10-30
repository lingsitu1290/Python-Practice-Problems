"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    # >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    coor = get_zero_coor(matrix) 

    if coor:
        y = coor[0]
        x = coor[1]

        for i in range(len(matrix[y])):
            matrix[y][i] = 0

        for j in range(len(matrix)):
            matrix[j][x] = 0

        return matrix
    return


def get_zero_coor(matrix):

    """Helper function to get the coordinate where 0 is located."""

    for i, lst in enumerate(matrix):
        for j, item in enumerate(lst):
            if item == 0:
                return i, j


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! YOU'RE DOING GREAT!\n"
