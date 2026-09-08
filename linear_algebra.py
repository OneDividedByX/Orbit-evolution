from math import cos, sin

def sum_vectors(vector1: list[float], vector2: list[float]):
    """Sum two vectors.
    Args:
        vector1 (list[float]): The first vector.
        vector2 (list[float]): The second vector.
    """
    return [vector1[i] + vector2[i] for i in range(len(vector1))]

def mult_scalar(scalar: float, vector: list[float]):
    """Multiply a vector by a scalar.
    Args:
        scalar (float): The scalar to multiply by.
        vector (list[float]): The vector to multiply.
    """
    return [scalar * vector[i] for i in range(len(vector))]

def dot_product(vector1: tuple[float, float], vector2: tuple[float, float]):
    return sum(x * y for x, y in zip(vector1, vector2))

def rotate_vector(vector: tuple[float, float], angle: float):
    """Rotate a vector by a given angle in radians."""    
    x, y = vector
    return (x * cos(angle) - y * sin(angle), x * sin(angle) + y * cos(angle))

def getNormal_vector(vector: tuple[float, float]):
    """Get a normal vector (perpendicular) to the given vector."""
    return (-vector[1], vector[0])

def norm_L2(vector: list[float]):
    return (sum(x**2 for x in vector)) ** 0.5

def distance(point1: list[float], point2: list[float], norm: str = 'L2'):
    if norm == 'L2':
        return norm_L2(sum_vectors(point1, mult_scalar(-1, point2)))
    else:
        raise ValueError("Unsupported norm")

def unit_vector(vector: tuple[float, float]):
    vector_norm = norm_L2(vector)
    if vector_norm == 0:
        raise ValueError("Cannot compute unit vector of the zero vector")
    return mult_scalar(1 / vector_norm, vector)