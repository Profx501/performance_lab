import sys
from typing import List


def point_inside_circle(path_circle: str, path_points: str) -> None:
    """
    Функция рассчитывает положение точки относительно
    окружности.
    """
    with open(path_circle, "r") as f:
        circle: List[str] = f.readlines()
        center_x, center_y = list(map(int, circle[0].strip().split()))
        radius = int(circle[1].strip())
    with open(path_points, "r") as f:
        for point in f:
            x, y = list(map(int, point.strip().split()))
            if (x - center_x) ** 2 + (y - center_y) ** 2 > radius ** 2:
                print(2, end="\n")
            elif (x - center_x) ** 2 + (y - center_y) ** 2 < radius ** 2:
                print(1, end="\n")
            else:
                print(0)


if __name__ == "__main__":
    try:
        path_circle = sys.argv[1]
        path_points = sys.argv[2]
        point_inside_circle(path_circle, path_points)
    except IndexError:
        print(
            "Вы забыли ввести два аргумента! Путь к файлу с координатами ",
            "окружности и координатами точек."
        )
