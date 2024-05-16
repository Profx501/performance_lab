import json
import sys
from typing import Any, Dict, List


def recursion(
        tests: List[Dict[str, Any]], values: Dict[str, Dict[str, Any]]
) -> None:
    """
    Рекурсивная функция для обхода словаря и заполнения
    тестовыми данными.
    """
    for d in tests:
        if "value" in d:
            d["value"] = values.get(d["id"])["value"]
        if "values" in d:
            recursion(d["values"], values)


def form_report(path_tests: str, path_values: str, path_report: str) -> None:
    """
    Функция считывает данные и результаты тестирования,
    формирует отчет и сохраняет в выбранный файл.
    """
    with open(path_tests, "r") as f:
        tests = json.load(f)

    with open(path_values, "r") as f:
        values = json.load(f)

    values_dict: Dict[str, Any] = {r['id']: r for r in values["values"]}
    recursion(tests["tests"], values_dict)

    with open(path_report, 'w') as f:
        json.dump(tests, f, indent=2)


if __name__ == "__main__":
    try:
        path_tests: str = sys.argv[1]
        path_values: str = sys.argv[2]
        path_report: str = sys.argv[3]
        form_report(path_tests, path_values, path_report)
    except IndexError:
        print(
            "Вы забыли ввести три аргумента!",
            "Путь к файлу с тестовыми данными, путь к файлу с",
            "результатом тестирования, путь куда сохранить файл с отчетом."
        )
