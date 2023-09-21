import json
import re
import os
import sys


class DataProcessor:
    def __init__(self, data_file, replacement_file, output_file):
        self.data_file = data_file
        self.replacement_file = replacement_file
        self.output_file = output_file

    def load_data(self, file_path):
        with open(file_path) as f:
            return json.load(f)

    def process_data(self):
        replacements = self.load_data(self.replacement_file)
        data = self.load_data(self.data_file)

        new_replacements = self.filter_and_clean_replacements(replacements)
        new_data = self.replace_data(data, new_replacements)

        self.save_data(new_data)

    def filter_and_clean_replacements(self, replacements):
        filtered_replacements = [r for r in replacements if r["source"] is not None]
        unique_replacements = {}

        for replacement in filtered_replacements:
            if replacement["replacement"] not in unique_replacements:
                unique_replacements[replacement["replacement"]] = replacement["source"]

        return {k: v for k, v in sorted(unique_replacements.items(), key=lambda item: len(item[1]), reverse=True)}

    def replace_data(self, data, replacements):
        new_data = data.copy()

        for rep_key, rep_value in replacements.items():
            regex = re.compile(re.escape(rep_key))
            new_data = [regex.sub(rep_value, message) for message in new_data]

        return [new_message for orig_message, new_message in zip(data, new_data) if orig_message != new_message]

    def save_data(self, data):
        with open(self.output_file, "w") as f:
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

    processor = DataProcessor(data_file, replacement_file, output_file)
    processor.process_data()
    print("Обработка данных завершена. Результат сохранен в файле:", output_file)


if __name__ == "__main__":
    program_start()