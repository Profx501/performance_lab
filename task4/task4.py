import sys
from typing import List


def all_elements(array: List[int]) -> None:
    """
    Функция выводит минимальное количество ходов, требуемых для
    приведения всех элементов к одном числу.
    """
    digit: int = round(sum(array)/len(array))
    counter: int = 0
    for element in array:
        counter += abs(digit - element)
    print(counter)


if __name__ == "__main__":
    try:
        path_file: str = sys.argv[1]
        with open(path_file, "r") as f:
            new_array: List[int] = [int(i.strip()) for i in f]
            all_elements(new_array)
    except IndexError:
        print("Вы забыли передать аргументом путь к файлу!")
