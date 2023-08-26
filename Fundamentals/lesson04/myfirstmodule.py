width = 5
height = 4


def calculate_area(width: int, height: int) -> int:
    area = width * height
    return area

area = calculate_area(width=width, height=height)

print(f"Area = {area}")
