import sys


def circular_array(n: int, m: int) -> str:
    """
    Функция выводит путь, по которому, двигаясь интервалом длины
    m по заданному массиву, концом будет являться первый элемент.
    """
    path: str = ""
    array: list[int] = [*range(1, n + 1)]
    x: int = 0  # первый элемент интервала
    while True:
        s = x % n
        path += str(array[s])
        if array[(s + m - 1) % n] == array[0]:
            # (s + m - 1) % n последний элемент интервала.
            return path
        x += m - 1


if __name__ == "__main__":
    try:
        n: int = int(sys.argv[1])
        m: int = int(sys.argv[2])
        print(circular_array(n, m))
    except IndexError:
        print("Вы забыли ввести аргументы n и m!")
