import json
import re
import os
import sys
import unittest


class DataProcessor:
    def __init__(self, data_file, replacement_file, output_file):
        self.data_file = data_file
        self.replacement_file = replacement_file
        self.output_file = output_file

    def _load_data(self, file_path):
        with open(file_path) as f:
            # print(file_path)
            return json.load(f)
    def _save_data(self, data):
        with open(self.output_file, "w") as f:
            json.dump(data, f, ensure_ascii=False)


    def _clean_replacements(self, replacements):
        unique_replacements = {}

        for replacement in reversed(replacements):
            if replacement["replacement"] not in unique_replacements:
                unique_replacements[replacement["replacement"]] = replacement["source"]

        return unique_replacements
    def _replace_data(self, data, replacements):
        new_data = data.copy()

        for rep_key, rep_value in replacements.items():
            if rep_value is None :
                new_data = [item for item in new_data if item != rep_key]
                continue

            else:
                regex = re.compile(re.escape(rep_key))
                # print(regex)
                new_data = [regex.sub(rep_value, message) for message in new_data]

        return new_data


    def process_data(self):
        # Загружаем данные замен из файла replacement_file
        replacements = self._load_data(self.replacement_file)

        # Загружаем исходные данные из файла data_file
        data = self._load_data(self.data_file)

        # Очищаем набор замен, удаляя дубликаты и значения с пустыми источниками,
        # а также сортируем замены в порядке убывания их длины
        new_replacements = self._clean_replacements(replacements)

        # Производим замену исходного текста в data, используя очищенные замены new_replacements
        new_data = self._replace_data(data, new_replacements)

        # Сохраняем измененные данные в файл output_file
        self._save_data(new_data)
        return new_data

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

def program_start(data_file, replacement_file, output_file):

    # data_file = get_file_path("Пожалуйста, введите путь к файлу data.json: ")
    #
    # replacement_file = get_file_path("Пожалуйста, введите путь к файлу replacement.json: ")
    #
    # output_file = input("Пожалуйста, введите имя и/или путь для файла вывода (result.json): ")

    processor = DataProcessor(data_file, replacement_file, output_file)

    print("Обработка данных завершена. Результат сохранен в файле:", output_file)
    data=processor.process_data()

    return    data






if __name__ == "__main__":
    program_start("data.json","replacement.json","result.json")