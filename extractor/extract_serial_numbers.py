import re
import os

def extract_serial_numbers(input_file, output_file):
    # Паттерн для поиска серийных номеров
    pattern = r'\b([A-Z0-9-]{10,})\b'
    
    # Проверка существования входного файла
    if not os.path.isfile(input_file):
        print(f"Файл {input_file} не найден.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    serial_numbers = []

    # Обработка каждой строки в файле
    for line in lines:
        matches = re.findall(pattern, line)
        serial_numbers.extend(matches)

    # Сохранение серийных номеров в выходной файл
    with open(output_file, 'w', encoding='utf-8') as f:
        for number in serial_numbers:
            f.write(number + '\n')

    print(f"Серийные номера успешно извлечены в файл {output_file}.")

# Указываем имена входного и выходного файлов
input_file = 'paste.txt'
output_file = 'serial_numbers.txt'

# Вызов функции для извлечения серийных номеров
extract_serial_numbers(input_file, output_file)