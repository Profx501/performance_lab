# Performance Lab

## Описание
- Task1 - Скрипт выводит путь, по которому, двигаясь интервалом длины
m по заданному круговой массиву, концом будет являться первый элемент.
- Task2 - Скрипт рассчитывает положение точки относительно
окружности.
- Task3 - Скрипт формирует отчет  на основании структуры для построения отчета прошедших
тестов и результатов пройденных тестов.
- Task4 - Скрипт выводит минимальное количество ходов, требуемых для
приведения всех элементов к одному числу.


## Технологии
- Python
- Flake8
- Isort
- Mypy

## Запуск
Склонируйте репозиторий performance_lab на свой компьютер.
## Функционал
- Task1:
  - Перейти в директорию task1
  - Аргументами передать n и m:
    - Массив задается числом -> n
    - интервалом длины -> m
  - Windows
   ```bash
   python task1.py 4 3
   ```
   - Linux/macOS
   ```bash
   python3 task1.py 4 3
   ```
- Task2:
  - Перейти в директорию task2
  - Аргументами передать:
    - Путь к файлам с координатами окружности.
    - Путь к файлам с координатами точек.
  - Пример структуры файлa circle.txt:
   ```bash
   1 1
   5
   ```
  - Пример структуры файлa dot.txt:
   ```bash
   0 0
   1 6
   6 6
   ```
  - Команда для запуска на Windows
   ```bash
   python task2.py C:/Dev/performance_lab/task2/circle.txt C:/Dev/performance_lab/task2/dot.txt
   ```
   - Команда для запуска на Linux/macOS
   ```bash
   python3 task2.py C:/Dev/performance_lab/task2/circle.txt C:/Dev/performance_lab/task2/dot.txt
   ```
- Task3:
  - Перейти в директорию task3
  - Аргументами передать:
    - Путь к файлу с тестовыми данными.
    - Путь к файлу с результатом тестирования.
    - Путь куда сохранить файл с отчетом.
    - ФОРМАТ ФАЙЛОВ JSON!!!
  - Команда для запуска на Windows
   ```bash
    python task3.py C:/Dev/performance_lab/task3/tests.json C:/Dev/performance_lab/task3/values.json C:/Dev/performance_lab/task3/report.json
   ```
   - Команда для запуска на Linux/macOS
   ```bash
    python3 task3.py C:/Dev/performance_lab/task3/tests.json C:/Dev/performance_lab/task3/values.json C:/Dev/performance_lab/task3/report.json
   ```
- Task4:
  - Перейти в директорию task4
  - Аргументам передать:
    - Путь к файлу с элементами массива.
  - Пример структуры файлa numbers.txt:
   ```bash
   1
   10
   2
   9
   ```
  - Команда для запуска на Windows
   ```bash
   python task4.py C:/Dev/performance_lab/task4/numbers.txt
   ```
   - Команда для запуска на Linux/macOS
   ```bash
   python3 task4.py C:/Dev/performance_lab/task4/numbers.txt
   ```
