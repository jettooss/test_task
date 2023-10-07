
import os
import unittest
import json

from main import program_start
from main import DataProcessor

class TestProcessDataNew(unittest.TestCase):

    def setUp(self):
        self.instance = DataProcessor(None, None, None)  # Создаем экземпляр класса
        self.test_file = "test_input.json"  # Тестовый файл
        self.test_data = {"test": "data"}  # Тестовые данные
        self.replacements = [  # Замены
            {"replacement": "test1", "source": "src1"},
            {"replacement": "test2", "source": None},
            {"replacement": "test1", "source": "src3"}
        ]
    def test_save_data(self):
        # Сохранения данных
        self.instance.output_file = self.test_file  # Предполагается, что у DataProcessor есть атрибут output_file
        self.instance._save_data(self.test_data)

        # Чтение файла и проверка на то что данные те же
        with open(self.test_file, 'r') as f:
            loaded_data = json.load(f)
        self.assertEqual(loaded_data, self.test_data)  # Проверка результата

    def test_load_data(self):
        # Загрузка данных
        data = self.instance._load_data(  self.test_file )
        # Проверка результата
        self.assertEqual(data, {"test": "data"})


    def test_clean_replacements(self):
        # Очистка замен
        unique_replacements = self.instance._clean_replacements(self.replacements)
        # Проверка результата
        self.assertEqual(unique_replacements["test1"], "src3")
        self.assertEqual(unique_replacements["test2"], None)

    def test_replace_data(self):
        # Тест замены данных
        data = ["This is a test1", "This is a test2", "This is a test1"]
        replacements = {"test1": "replacement1", "test2": "replacement2"}
        new_data = self.instance._replace_data(data, replacements)
        expected_data = ["This is a replacement1", "This is a replacement2", "This is a replacement1"]
        # Проверка результата
        self.assertEqual(new_data, expected_data)

    def test_replace_data_with_none(self):
        # Тест замены данных с None
        data = ["test", "This is another", "Hello, world!"]
        replacements = {"test": None, "world": "1"}
        new_data = self.instance._replace_data(data, replacements)
        # В этом случае "test" должен быть удален из данных
        expected_data = ['This is another', 'Hello, 1!']
        # Проверка результата
        self.assertEqual(new_data, expected_data)

    def test_process_data_thewhite(self):
        # Тест обработки данных
        actual_output = program_start('data.json', 'replacement.json', 'output1.json')
        expected_output = self.load_data_from_file('initial-data.json')
        # Проверка результата
        self.assertEqual(actual_output, expected_output)

    def test_process_data_new(self):
        # Новый тест обработки данных
        actual_output = program_start('my_data.json', 'replace.json', 'output2.json')
        expected_output = self.load_data_from_file('expected_output_data.json')
        # Проверка результата
        self.assertEqual(actual_output, expected_output)

    # Загружаем данные из файла
    def load_data_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data


if __name__ == "__main__":
    unittest.main()


