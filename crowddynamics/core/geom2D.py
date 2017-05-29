import numba
from numba import f8


@numba.jit(f8(f8[:, :]), nopython=True, nogil=True, cache=True)
def polygon_area(vertices):
    r"""Shoelace formula for computing area of polygon
    
    .. math::
        A = \sum_{i=1}^{n} x_i \left(y_{i+1} - y_{i-1}\right), \quad i\mod n

    References:
        - https://en.wikipedia.org/wiki/Shoelace_formula
        - https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon/717367#717367
        - https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
    
    Args:
        vertices (numpy.ndarray): Vertices of the polygon

    Returns:
        float: Area of the polygon
    """
    n = len(vertices)
    area = 0.0
    if n < 3:
        return area
    x, y = vertices[:, 0], vertices[:, 1]
    for i in range(1, n-1):
        area += x[i] * (y[i + 1] - y[i - 1])
    # i=n-1
    area += x[n-1] * (y[0] - y[n - 2])
    # i=n
    area += x[0] * (y[1] - y[n - 1])
    return 0.5 * abs(area)