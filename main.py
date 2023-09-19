import json
import sys
import os
import re


def process_data(data_file, replacement_file, output_file):

    with open(replacement_file) as f:
        replacements = json.load(f)

    with open(data_file) as f:
        data = json.load(f)

    filtered_replacements = [replacement for replacement in replacements if replacement["source"] is not None]
    new_replacements = {}

    for replacement in filtered_replacements:
        if replacement["replacement"] in new_replacements:
            filtered_replacements.remove(replacement)
        else:
            new_replacements[replacement["replacement"]] = replacement["source"]

    sorted_replacements = {k: v for k, v in sorted(new_replacements.items(), key=lambda item: len(item[1]), reverse=True)}

    new_data = data.copy()

    for rep_key, rep_value in sorted_replacements.items():
        regex = re.compile(re.escape(rep_key))
        new_data = [regex.sub(rep_value, message) for message in new_data]

    new_data = [new_message for orig_message, new_message in zip(data, new_data) if orig_message != new_message]
    print(new_data)

    with open(output_file, "w") as f:
        json.dump(data, f, ensure_ascii=False)


def get_file_path(prompt):
    while True:
        try:
            file_path = input(prompt)

            if os.path.exists(file_path):
                return file_path
            else:
                print(f"Файл не найден: {file_path}")
                continue
        except KeyboardInterrupt:
            print("\nВыход из программы")
            sys.exit()


def program_start():
    data_file = get_file_path("Пожалуйста, введите путь к файлу data.json: ")
    replacement_file = get_file_path("Пожалуйста, введите путь к файлу replacement.json: ")
    output_file = input("Пожалуйста, введите имя и/или путь для файла вывода (result.json): ")

    process_data("data.json", "replacement.json", "re1.json")
    # print("Обработка данных завершена. Результат сохранен в файле:", output_file)


if __name__ == "__main__":
    program_start()