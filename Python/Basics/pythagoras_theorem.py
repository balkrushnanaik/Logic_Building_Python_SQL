import math


def hypotenuse(a, b):
    """Return the hypotenuse for a right triangle with legs a and b."""
    return math.hypot(a, b)


def is_right_triangle(a, b, c, tol=1e-9):
    """Return True if a, b, c satisfy the Pythagorean theorem."""
    sides = sorted((a, b, c))
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tol


if __name__ == "__main__":
    try:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        print(f"Hypotenuse: {hypotenuse(a, b)}")
    except ValueError:
        print("Please enter numeric values.")
